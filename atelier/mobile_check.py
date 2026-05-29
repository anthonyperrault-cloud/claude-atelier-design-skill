#!/usr/bin/env python3
"""
atelier — mobile-readiness linter
=================================
Scans HTML/CSS/SCSS/JSX/TSX/Vue for patterns that quietly break small screens, so "mobile-first"
is verified, not just intended. Pairs with the mobile-first guidance in references/ux-accessibility.md
and references/layout-spacing.md.

A script cannot make the agent THINK mobile-first — that is an instruction. This catches the
evidence when it didn't: disabled zoom, missing viewport, fixed widths that overflow, tiny input
fonts that trigger iOS zoom, touch targets under 44px, hover-only interaction, and fixed bars with
no safe-area inset.

Severity:
    ERROR  clear mobile/accessibility violation — fix it
    WARN   likely problem — review it
    INFO   worth a glance (summarized, not listed line-by-line, to avoid noise)

Usage:
    python3 mobile_check.py <file-or-directory>
    python3 mobile_check.py ./src

Exit 0 = no ERRORs. Exit 1 = ERRORs found.
"""

import sys
import re
from pathlib import Path

EXTS = {".html", ".htm", ".css", ".scss", ".sass", ".jsx", ".tsx", ".vue", ".js", ".ts"}

# Per-line checks: (compiled regex, severity, message, optional value-test)
LINE_CHECKS = [
    (re.compile(r"user-scalable\s*=\s*no", re.I), "ERROR",
     "zoom disabled (user-scalable=no) — blocks pinch-zoom, an accessibility violation", None),
    (re.compile(r"maximum-scale\s*=\s*1(?:\.0)?\b", re.I), "ERROR",
     "zoom capped (maximum-scale=1) — prevents users from zooming", None),
    (re.compile(r"(?<![-\w])(?:width|min-width)\s*:\s*(\d{3,})px", re.I), "WARN",
     "fixed pixel width — can overflow small screens; prefer %, rem, max-width, or fr",
     lambda v: int(v) >= 480),
    (re.compile(r"font-size\s*:\s*(\d{1,2})(?:px)?\b", re.I), "WARN",
     "font-size below 16px — if this is an input/select/textarea it triggers iOS auto-zoom",
     lambda v: int(v) < 16),
    (re.compile(r"(?:height|min-height)\s*:\s*(\d{1,2})px", re.I), "INFO",
     "height under 44px — if this is a touch target it is below the 44px minimum",
     lambda v: int(v) < 44),
    (re.compile(r"position\s*:\s*fixed", re.I), "INFO",
     "position:fixed — if a top/bottom bar, add env(safe-area-inset-*) for notch/home-indicator", None),
    (re.compile(r"white-space\s*:\s*nowrap", re.I), "INFO",
     "white-space:nowrap — can force horizontal overflow if applied to long text", None),
    (re.compile(r":hover", re.I), "INFO",
     ":hover used — verify a touch/focus equivalent exists (no hover on touch devices)", None),
]


def scan_text_file(path: Path, root: Path):
    findings = []          # (severity, relpath, lineno, message)
    info_counts = {}       # message -> count  (INFO is summarized, not listed)
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    rel = path.relative_to(root) if root in path.parents or root == path.parent else path

    # Per-file: HTML must declare a responsive viewport
    if path.suffix.lower() in {".html", ".htm"}:
        if not re.search(r'<meta[^>]*name=["\']viewport["\']', text, re.I):
            findings.append(("ERROR", rel, 0,
                             "no responsive viewport meta tag — add "
                             "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"))

    for i, line in enumerate(lines, 1):
        for rx, sev, msg, test in LINE_CHECKS:
            m = rx.search(line)
            if not m:
                continue
            if test is not None:
                if not m.groups():
                    continue
                try:
                    if not test(m.group(1)):
                        continue
                except (ValueError, IndexError):
                    continue
            if sev == "INFO":
                info_counts[msg] = info_counts.get(msg, 0) + 1
            else:
                findings.append((sev, rel, i, msg))
    return findings, info_counts


def main():
    if len(sys.argv) != 2:
        print("usage: python3 mobile_check.py <file-or-directory>")
        return 1

    target = Path(sys.argv[1]).resolve()
    if not target.exists():
        print(f"path not found: {target}")
        return 1

    root = target if target.is_dir() else target.parent
    files = [target] if target.is_file() else [
        p for p in sorted(target.rglob("*")) if p.suffix.lower() in EXTS and p.is_file()
    ]

    all_findings = []
    info_totals = {}
    for f in files:
        try:
            findings, infos = scan_text_file(f, root)
        except Exception as e:
            print(f"  could not read {f}: {e}")
            continue
        all_findings.extend(findings)
        for msg, n in infos.items():
            info_totals[msg] = info_totals.get(msg, 0) + n

    errors = [x for x in all_findings if x[0] == "ERROR"]
    warns = [x for x in all_findings if x[0] == "WARN"]

    print(f"atelier mobile-readiness check — {target}")
    print(f"  files scanned: {len(files)}")
    print(f"  errors: {len(errors)}   warnings: {len(warns)}   info notes: {sum(info_totals.values())}\n")

    for sev, rel, lineno, msg in sorted(errors + warns, key=lambda x: (x[0], str(x[1]), x[2])):
        loc = f"{rel}:{lineno}" if lineno else str(rel)
        print(f"  [{sev}]  {loc}\n          {msg}")

    if info_totals:
        print("\n  info (review if relevant):")
        for msg, n in sorted(info_totals.items(), key=lambda x: -x[1]):
            print(f"    ({n}x) {msg}")

    print()
    if errors:
        print(f"  result: {len(errors)} error(s) to fix. Mobile-first is not satisfied yet.")
        return 1
    if warns:
        print(f"  result: no errors, {len(warns)} warning(s) to review — complete with caveats.")
        return 0
    print("  result: COMPLETE — no mobile-hostile patterns detected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
