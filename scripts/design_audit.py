#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import struct
from pathlib import Path


GALLERY_ASSETS = [
    "assets/hero-command-center.png",
    "assets/hero-global-filmmaker-mode.png",
    "assets/infographic-skill-capabilities.png",
    "assets/infographic-cdn-delivery-map.png",
    "assets/infographic-reference-role-map.png",
    "assets/infographic-production-delivery.png",
    "assets/infographic-professional-qc-stack.png",
]

CORE_BITMAP_ASSETS = [
    *GALLERY_ASSETS,
    "assets/hero-cinematic.png",
    "assets/skill-os-infographic.png",
    "assets/skill-map-cinematic.png",
]


def png_dimensions(path: Path) -> tuple[int, int] | None:
    with path.open("rb") as handle:
        header = handle.read(24)
    if len(header) < 24 or header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
        return None
    return struct.unpack(">II", header[16:24])


def check_png_asset(
    root: Path,
    rel: str,
    label: str,
    errors: list[str],
    *,
    min_bytes: int = 100_000,
    min_width: int = 1200,
    min_height: int = 650,
) -> None:
    path = root / rel
    if not path.exists():
        errors.append(f"missing asset: {rel}")
        return
    if path.stat().st_size < min_bytes:
        errors.append(f"{rel} appears too small for a real {label} image")
    size = png_dimensions(path)
    if size is None:
        errors.append(f"{rel} is not a valid PNG")
        return
    width, height = size
    if width < min_width or height < min_height:
        errors.append(f"{rel} is too small for README display ({width}x{height})")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", nargs="?", default=".")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    root = Path(args.repo).resolve()
    errors = []

    readme = root / "README.md"
    if not readme.exists():
        errors.append("README.md missing")
    else:
        text = readme.read_text(encoding="utf-8")
        lines = text.splitlines()
        if len(lines) < 80:
            errors.append(f"README.md is too short or collapsed ({len(lines)} lines)")
        long_lines = [i + 1 for i, line in enumerate(lines) if len(line) > 500]
        if long_lines:
            errors.append("README.md has lines over 500 chars: " + ", ".join(map(str, long_lines[:10])))
        for required in [
            "# Seedance 2.0 Skill OS 中文精简版",
            "zh-QUICKSTART.md",
            "zh-USAGE.md",
            "docs/README.zh.md",
            "## 应该在 Codex 里用，还是在 VS Code 里跑",
            "## 快速安装到 Codex",
            "## 这个项目能做什么",
            "## 中文精简后的结构",
            "## 最小使用流程",
            "## 本次精简移除了什么",
            "## 维护时常用检查",
            "skills/seedance-vocab-zh",
            "skills/seedance-examples-zh",
            "references/vocab/zh.md",
            "python scripts/install_codex_skill.py --force",
            "$seedance-20",
        ]:
            if required not in text:
                errors.append(f"README.md missing `{required}`")
        forbidden = [
            "docs/README.ja.md",
            "docs/README.ko.md",
            "seedance-examples-ja",
            "seedance-examples-ko",
            "seedance-vocab-ja",
            "seedance-vocab-ko",
            "seedance-vocab-es",
            "seedance-vocab-ru",
            "references/multilingual-community-examples.md",
        ]
        for token in forbidden:
            if token in text:
                errors.append(f"README.md still references removed translation entry `{token}`")

    redesign_doc = root / "docs" / "frontend-redesign.md"
    if not redesign_doc.exists():
        errors.append("missing docs/frontend-redesign.md")
    else:
        doc_text = redesign_doc.read_text(encoding="utf-8").lower()
        if "text-rich infographics" not in doc_text or "infographic-cdn-delivery-map.png" not in doc_text:
            errors.append("docs/frontend-redesign.md missing text-rich gallery guidance")

    design_system = root / "references" / "frontend-design-system.md"
    if not design_system.exists():
        errors.append("missing references/frontend-design-system.md")
    else:
        ds_text = design_system.read_text(encoding="utf-8").lower()
        if "text-rich infographics" not in ds_text or "reject garbled" not in ds_text:
            errors.append("references/frontend-design-system.md missing text-rich infographic quality rules")

    for rel in CORE_BITMAP_ASSETS:
        check_png_asset(root, rel, "README visual", errors)

    for rel in ["assets/hero-dark.svg", "assets/hero-light.svg", "assets/skill-map.svg"]:
        path = root / rel
        if not path.exists():
            errors.append(f"missing asset: {rel}")
            continue
        svg = path.read_text(encoding="utf-8", errors="ignore")
        if "<svg" not in svg:
            errors.append(f"{rel} is not an SVG")
        if "<title>" not in svg or "<desc>" not in svg:
            errors.append(f"{rel} missing accessible title/desc")
        if re.search(r"<script|href=[\"\']https?://|xlink:href=[\"\']https?://", svg, re.I):
            errors.append(f"{rel} must not include scripts or external resources")
        if "linearGradient" in svg or "feGaussianBlur" in svg:
            errors.append(f"{rel} must follow the editorial standard: no gradients or blur filters")
        if "Georgia" not in svg or "ui-monospace" not in svg:
            errors.append(f"{rel} missing the editorial serif/monospace type stacks")

    if errors:
        print("Design audit errors:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Design audit passed: README and visual assets are structured and accessible.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
