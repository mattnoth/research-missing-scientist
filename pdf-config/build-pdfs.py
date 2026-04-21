#!/usr/bin/env python3
"""Build all PDFs for the Missing Scientists dossier.

Requires: pandoc, weasyprint (both assumed installed).
Run from the repo root: python3 pdf-config/build-pdfs.py
"""

import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PDF_OUT = ROOT / "pdf-output"
PDF_CFG = ROOT / "pdf-config"
CASES_DIR = ROOT / "cases"

# Case file order matches the dossier case index
CASE_ORDER = [
    "chavez", "casias", "reza", "garcia", "mccasland",
    "grillmair", "loureiro", "hicks", "maiwald", "thomas", "eskridge",
]

ANALYSIS_FILES = [
    "analysis/connection-analysis.md",
    "analysis/hypotheses.md",
    "analysis/foreign-intel-layer.md",
]

# Appendix directories in order
APPENDIX_GROUPS = [
    ("Primary Source Excerpts", "appendices/primary-sources"),
    ("Foreign Coverage", "appendices/foreign-coverage"),
    ("Named Expert Commentary", "appendices/named-expert-commentary"),
]

LOG_FILES = [
    "logs/research-log.md",
    "logs/contradictions.md",
    "logs/known-unknowns.md",
]


def run_pandoc(input_path, output_path, extra_args=None):
    """Run pandoc with weasyprint engine."""
    cmd = [
        "pandoc",
        str(input_path),
        "-o", str(output_path),
        "--pdf-engine=weasyprint",
        f"--css={PDF_CFG / 'print.css'}",
        "--toc" if output_path.name == "missing-scientists-dossier.pdf" else "",
        "--toc-depth=3" if output_path.name == "missing-scientists-dossier.pdf" else "",
    ]
    # Remove empty strings
    cmd = [c for c in cmd if c]
    if extra_args:
        cmd.extend(extra_args)
    print(f"  pandoc -> {output_path.name}")
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    if result.returncode != 0:
        print(f"  ERROR: {result.stderr[:500]}")
        return False
    return output_path.exists() and output_path.stat().st_size > 0


def read_file(relpath):
    """Read a file relative to ROOT."""
    p = ROOT / relpath
    if p.exists():
        return p.read_text(encoding="utf-8")
    print(f"  WARNING: {relpath} not found")
    return ""


def collect_appendix_files(base_dir):
    """Collect all .md files under a directory, sorted."""
    base = ROOT / base_dir
    if not base.exists():
        return []
    files = sorted(base.rglob("*.md"))
    return files


def build_cover_page():
    """Build HTML cover page."""
    return """<div class="cover-page">

# Deaths and Disappearances of U.S. Defense and Advanced-Research Scientists

<div class="subtitle">Research Dossier</div>

<div class="author">Matt Noth</div>

<div class="date">April 21, 2026</div>

<div class="notice">

**Living document** — see CHANGELOG.md for version history. This is not a publication or journalism product; it is a personal research compilation. Sources are categorized by tier (T1 primary through T7 foreign state-affiliated). Claims carry confidence ratings: Confirmed, Reported, Alleged, or Speculated.

**Source Tier Key:**
T1 = Primary (law enforcement, court filings, official statements) |
T2 = Secondary (mainstream news) |
T3 = Tertiary (aggregators) |
T4 = Social media / forums |
T5 = Anonymous / single-source |
T6 = Conspiracy-adjacent media |
T7 = Foreign state-affiliated media

**Confidence Ratings:**
[Confirmed] = Multiple independent T1/T2 sources agree |
[Reported] = At least one T1/T2 source; not independently verified |
[Alleged] = Single source or T4-T7; unverified |
[Speculated] = No sourcing; included for transparency only

</div>

</div>
"""


def build_master_markdown():
    """Assemble the full dossier markdown."""
    parts = []

    # Cover page
    parts.append(build_cover_page())

    # Main dossier (abstract, executive summary, methodology, case index, etc.)
    parts.append(read_file("dossier.md"))

    # Separator before cases
    parts.append("\n\n---\n\n# Part II: Individual Case Files\n\n")

    # Case files in order
    for slug in CASE_ORDER:
        content = read_file(f"cases/{slug}.md")
        if content:
            parts.append(f"\n\n---\n\n{content}")

    # Analysis
    parts.append("\n\n---\n\n# Part III: Cross-Case Analysis\n\n")
    for f in ANALYSIS_FILES:
        content = read_file(f)
        if content:
            parts.append(f"\n\n---\n\n{content}")

    # Appendices
    parts.append("\n\n---\n\n# Part IV: Appendices\n\n")
    for group_name, base_dir in APPENDIX_GROUPS:
        parts.append(f"\n\n## {group_name}\n\n")
        files = collect_appendix_files(base_dir)
        for fp in files:
            content = fp.read_text(encoding="utf-8")
            # Use relative path as a subheading context
            rel = fp.relative_to(ROOT)
            parts.append(f"\n\n---\n\n<!-- Source: {rel} -->\n\n{content}")

    # Logs as trailing appendices
    parts.append("\n\n---\n\n# Part V: Methodology Logs\n\n")
    for f in LOG_FILES:
        content = read_file(f)
        if content:
            parts.append(f"\n\n---\n\n{content}")

    return "\n".join(parts)


def build_case_pdf(slug):
    """Build individual case PDF."""
    case_file = CASES_DIR / f"{slug}.md"
    if not case_file.exists():
        print(f"  WARNING: {slug}.md not found")
        return False

    # Build a small markdown with header and case content
    parts = []
    parts.append(f"---\ntitle: Case File — {slug.replace('-', ' ').title()}\nauthor: Matt Noth\ndate: April 21, 2026\n---\n\n")
    parts.append(case_file.read_text(encoding="utf-8"))

    # Append relevant primary-source appendix entries
    ps_dir = ROOT / "appendices" / "primary-sources" / slug
    if ps_dir.exists():
        ps_files = sorted(ps_dir.glob("*.md"))
        if ps_files:
            parts.append("\n\n---\n\n## Appendix: Primary Source Excerpts\n\n")
            for f in ps_files:
                parts.append(f"\n\n---\n\n{f.read_text(encoding='utf-8')}")

    master = "\n".join(parts)
    master_path = PDF_OUT / "cases" / f"{slug}-master.md"
    master_path.write_text(master, encoding="utf-8")

    out_path = PDF_OUT / "cases" / f"{slug}.pdf"
    ok = run_pandoc(master_path, out_path)
    master_path.unlink()  # Clean up temp file
    return ok


def build_diagram_svg(layer_filter, output_name):
    """Build a static SVG diagram from diagram-data.json."""
    data = json.loads((ROOT / "data" / "diagram-data.json").read_text())

    # Filter edges by layer
    layer_include = {
        "tight": {"tight"},
        "medium": {"tight", "medium"},
        "corkboard": {"tight", "medium", "corkboard"},
    }
    allowed_layers = layer_include[layer_filter]
    edges = [e for e in data["edges"] if e["layer"] in allowed_layers]

    # Collect referenced node IDs
    referenced_ids = set()
    for e in edges:
        referenced_ids.add(e["source"])
        referenced_ids.add(e["target"])

    nodes = [n for n in data["nodes"] if n["id"] in referenced_ids]

    # Layout: assign positions by type
    type_groups = {}
    for n in nodes:
        t = n["type"]
        if t not in type_groups:
            type_groups[t] = []
        type_groups[t].append(n)

    # SVG dimensions
    W, H = 1200, 900
    positions = {}

    # Position persons across the top
    persons = type_groups.get("person", [])
    for i, n in enumerate(persons):
        x = 80 + (i * (W - 160) // max(len(persons) - 1, 1))
        positions[n["id"]] = (x, 100)

    # Institutions in middle
    insts = type_groups.get("institution", [])
    for i, n in enumerate(insts):
        x = 80 + (i * (W - 160) // max(len(insts) - 1, 1))
        positions[n["id"]] = (x, 350)

    # Locations lower
    locs = type_groups.get("location", [])
    for i, n in enumerate(locs):
        x = 80 + (i * (W - 160) // max(len(locs) - 1, 1))
        positions[n["id"]] = (x, 550)

    # Programs at bottom
    progs = type_groups.get("program", [])
    for i, n in enumerate(progs):
        x = 80 + (i * (W - 160) // max(len(progs) - 1, 1))
        positions[n["id"]] = (x, 750)

    # Build SVG
    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" style="font-family: Helvetica, Arial, sans-serif; font-size: 9px;">',
        f'<rect width="{W}" height="{H}" fill="white"/>',
    ]

    # Draw edges
    layer_styles = {
        "tight": 'stroke="#333" stroke-width="1.5" stroke-dasharray="none" opacity="1"',
        "medium": 'stroke="#666" stroke-width="1" stroke-dasharray="6,3" opacity="0.7"',
        "corkboard": 'stroke="#c44" stroke-width="1" stroke-dasharray="2,3" opacity="0.4"',
    }
    for e in edges:
        s = positions.get(e["source"])
        t = positions.get(e["target"])
        if s and t:
            style = layer_styles[e["layer"]]
            svg_parts.append(f'<line x1="{s[0]}" y1="{s[1]}" x2="{t[0]}" y2="{t[1]}" {style}/>')

    # Draw nodes
    type_colors = {
        "person": "#2266aa",
        "institution": "#aa6622",
        "location": "#228844",
        "program": "#884488",
    }
    type_shapes = {
        "person": "circle",
        "institution": "rect",
        "location": "diamond",
        "program": "rect",
    }
    for n in nodes:
        pos = positions.get(n["id"])
        if not pos:
            continue
        x, y = pos
        color = type_colors.get(n["type"], "#666")
        label = n["label"]
        # Truncate long labels
        if len(label) > 30:
            label = label[:28] + "..."

        if n["type"] == "person":
            svg_parts.append(f'<circle cx="{x}" cy="{y}" r="18" fill="{color}" opacity="0.85"/>')
            svg_parts.append(f'<text x="{x}" y="{y+32}" text-anchor="middle" fill="#111" font-size="8px" font-weight="bold">{label}</text>')
        elif n["type"] == "location":
            svg_parts.append(f'<polygon points="{x},{y-16} {x+16},{y} {x},{y+16} {x-16},{y}" fill="{color}" opacity="0.85"/>')
            svg_parts.append(f'<text x="{x}" y="{y+28}" text-anchor="middle" fill="#111" font-size="8px">{label}</text>')
        else:
            svg_parts.append(f'<rect x="{x-40}" y="{y-12}" width="80" height="24" rx="4" fill="{color}" opacity="0.85"/>')
            svg_parts.append(f'<text x="{x}" y="{y+4}" text-anchor="middle" fill="white" font-size="7px">{label}</text>')

    # Legend
    ly = 20
    svg_parts.append(f'<text x="10" y="{ly}" font-weight="bold" font-size="11px">Legend — {output_name.replace("-", " ").title()}</text>')
    ly += 18

    # Node types
    svg_parts.append(f'<circle cx="20" cy="{ly}" r="6" fill="#2266aa"/>')
    svg_parts.append(f'<text x="32" y="{ly+4}" font-size="9px">Person</text>')
    svg_parts.append(f'<rect x="94" y="{ly-6}" width="12" height="12" rx="2" fill="#aa6622"/>')
    svg_parts.append(f'<text x="112" y="{ly+4}" font-size="9px">Institution</text>')
    svg_parts.append(f'<polygon points="200,{ly-6} 206,{ly} 200,{ly+6} 194,{ly}" fill="#228844"/>')
    svg_parts.append(f'<text x="212" y="{ly+4}" font-size="9px">Location</text>')
    svg_parts.append(f'<rect x="274" y="{ly-6}" width="12" height="12" rx="2" fill="#884488"/>')
    svg_parts.append(f'<text x="292" y="{ly+4}" font-size="9px">Program</text>')
    ly += 18

    # Edge types
    svg_parts.append(f'<line x1="10" y1="{ly}" x2="40" y2="{ly}" stroke="#333" stroke-width="1.5"/>')
    svg_parts.append(f'<text x="46" y="{ly+4}" font-size="9px">Tight (documented)</text>')
    svg_parts.append(f'<line x1="170" y1="{ly}" x2="200" y2="{ly}" stroke="#666" stroke-width="1" stroke-dasharray="6,3"/>')
    svg_parts.append(f'<text x="206" y="{ly+4}" font-size="9px">Medium (inferential)</text>')
    svg_parts.append(f'<line x1="340" y1="{ly}" x2="370" y2="{ly}" stroke="#c44" stroke-width="1" stroke-dasharray="2,3"/>')
    svg_parts.append(f'<text x="376" y="{ly+4}" font-size="9px">Corkboard (speculative)</text>')
    ly += 18

    # Confidence ratings
    svg_parts.append(f'<text x="10" y="{ly+4}" font-size="8px" fill="#555">Confidence: [Confirmed] = verified multi-source | [Reported] = single T1/T2 | [Alleged] = unverified | [Speculated] = no sourcing</text>')

    svg_parts.append('</svg>')
    return "\n".join(svg_parts)


def build_timeline_svg():
    """Build a timeline SVG from timeline-data.json."""
    data = json.loads((ROOT / "data" / "timeline-data.json").read_text())

    all_events = data["events"] + data.get("context_events", [])
    all_events.sort(key=lambda e: e["date"])

    W, H = 1400, 1000
    margin_top = 80
    margin_bottom = 40
    margin_left = 120
    margin_right = 40

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" style="font-family: Helvetica, Arial, sans-serif;">',
        f'<rect width="{W}" height="{H}" fill="white"/>',
        f'<text x="{W//2}" y="30" text-anchor="middle" font-size="16px" font-weight="bold">Timeline: Deaths and Disappearances of U.S. Defense Scientists (2022-2026)</text>',
    ]

    # Type colors
    type_colors = {
        "death": "#cc3333",
        "disappearance": "#cc8833",
        "investigation_milestone": "#3366aa",
        "suspect_arrested": "#339944",
        "body_found": "#993399",
        "other": "#666666",
        "media_event": "#888888",
        "political_event": "#aa6633",
        "institutional_statement": "#336688",
    }

    # Draw events as rows
    usable_h = H - margin_top - margin_bottom
    row_h = min(20, usable_h / len(all_events))
    text_x = margin_left

    for i, evt in enumerate(all_events):
        y = margin_top + i * row_h
        color = type_colors.get(evt["type"], "#666")
        is_context = "context" in evt.get("id", "")
        opacity = "0.6" if is_context else "1"

        # Date label
        svg.append(f'<text x="10" y="{y+4}" font-size="8px" fill="#444" opacity="{opacity}">{evt["date"]}</text>')

        # Color dot
        svg.append(f'<circle cx="{text_x - 10}" cy="{y}" r="4" fill="{color}" opacity="{opacity}"/>')

        # Description (truncated)
        desc = evt["description"]
        if len(desc) > 140:
            desc = desc[:137] + "..."
        conf = f' [{evt.get("confidence", "")}]' if "confidence" in evt else ""
        svg.append(f'<text x="{text_x}" y="{y+4}" font-size="7.5px" fill="#111" opacity="{opacity}">{desc}{conf}</text>')

    # Legend
    ly = H - 25
    lx = 10
    svg.append(f'<text x="{lx}" y="{ly}" font-weight="bold" font-size="9px">Event types:</text>')
    lx += 75
    for etype, color in type_colors.items():
        label = etype.replace("_", " ")
        svg.append(f'<circle cx="{lx}" cy="{ly-3}" r="4" fill="{color}"/>')
        svg.append(f'<text x="{lx+8}" y="{ly}" font-size="8px">{label}</text>')
        lx += len(label) * 5.5 + 25

    svg.append('</svg>')
    return "\n".join(svg)


def svg_to_pdf(svg_content, output_path, title):
    """Convert SVG to PDF via an HTML wrapper + weasyprint."""
    html = f"""<!DOCTYPE html>
<html><head>
<meta charset="utf-8"/>
<title>{title}</title>
<style>
  @page {{ size: letter landscape; margin: 0.5in; }}
  body {{ margin: 0; padding: 0; }}
  svg {{ width: 100%; height: auto; }}
</style>
</head><body>
{svg_content}
</body></html>"""

    html_path = output_path.with_suffix(".html")
    html_path.write_text(html, encoding="utf-8")

    cmd = ["pandoc", str(html_path), "-o", str(output_path),
           "--pdf-engine=weasyprint", "-f", "html"]
    print(f"  pandoc (svg->pdf) -> {output_path.name}")
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    html_path.unlink()
    if result.returncode != 0:
        print(f"  ERROR: {result.stderr[:500]}")
        return False
    return output_path.exists() and output_path.stat().st_size > 0


def main():
    os.makedirs(PDF_OUT / "cases", exist_ok=True)
    os.makedirs(PDF_OUT / "diagrams", exist_ok=True)

    results = {}

    # --- Task 3: Main dossier PDF ---
    print("\n[1/4] Building main dossier PDF...")
    master_md = build_master_markdown()
    master_path = PDF_OUT / "dossier-master.md"
    master_path.write_text(master_md, encoding="utf-8")
    ok = run_pandoc(master_path, PDF_OUT / "missing-scientists-dossier.pdf",
                    extra_args=["--toc", "--toc-depth=3",
                                f"--metadata-file={PDF_CFG / 'metadata.yaml'}"])
    master_path.unlink()
    results["dossier"] = ok

    # --- Task 4: Individual case PDFs ---
    print("\n[2/4] Building individual case PDFs...")
    for slug in CASE_ORDER:
        ok = build_case_pdf(slug)
        results[f"case-{slug}"] = ok

    # --- Task 5: Diagram PDFs ---
    print("\n[3/4] Building diagram PDFs...")
    for layer, name in [
        ("tight", "connection-diagram-tight"),
        ("medium", "connection-diagram-medium"),
        ("corkboard", "connection-diagram-corkboard"),
    ]:
        svg = build_diagram_svg(layer, name)
        out = PDF_OUT / "diagrams" / f"{name}.pdf"
        ok = svg_to_pdf(svg, out, f"Connection Diagram — {layer.title()} Layer")
        results[f"diagram-{layer}"] = ok

    # --- Task 6: Timeline PDF ---
    print("\n[4/4] Building timeline PDF...")
    svg = build_timeline_svg()
    out = PDF_OUT / "timeline.pdf"
    ok = svg_to_pdf(svg, out, "Timeline: Missing Scientists")
    results["timeline"] = ok

    # --- Report ---
    print("\n" + "=" * 60)
    print("PDF Generation Results")
    print("=" * 60)
    all_ok = True
    for name, ok in results.items():
        status = "OK" if ok else "FAILED"
        if not ok:
            all_ok = False
        # Get file size
        if ok:
            if "case-" in name:
                slug = name.replace("case-", "")
                p = PDF_OUT / "cases" / f"{slug}.pdf"
            elif "diagram-" in name:
                layer = name.replace("diagram-", "")
                p = PDF_OUT / "diagrams" / f"connection-diagram-{layer}.pdf"
            elif name == "timeline":
                p = PDF_OUT / "timeline.pdf"
            elif name == "dossier":
                p = PDF_OUT / "missing-scientists-dossier.pdf"
            else:
                p = None
            size = f" ({p.stat().st_size / 1024:.0f} KB)" if p and p.exists() else ""
        else:
            size = ""
        print(f"  {name}: {status}{size}")

    print()
    if all_ok:
        print("All PDFs generated successfully.")
    else:
        print("Some PDFs failed. Check errors above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
