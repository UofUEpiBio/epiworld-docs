#!/usr/bin/env python3

"""Generate a browsable example gallery from the upstream epiworld repository."""

from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path


ROOT_SHOWCASE_FILES = ("helloworld.cpp", "readme.cpp")
SUPPORTED_EXTENSIONS = {
    ".c",
    ".cc",
    ".cpp",
    ".cxx",
    ".h",
    ".hpp",
    ".md",
    ".py",
    ".R",
    ".r",
}
LANGUAGE_MAP = {
    ".c": "c",
    ".cc": "cpp",
    ".cpp": "cpp",
    ".cxx": "cpp",
    ".h": "cpp",
    ".hpp": "cpp",
    ".md": "markdown",
    ".py": "python",
    ".R": "r",
    ".r": "r",
}
GENERATED_PAGE_PREFIX = "example-"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate docs pages for examples from the epiworld repo."
    )
    parser.add_argument(
        "--source",
        default="epiworld-src",
        help="Path to the cloned upstream epiworld repository.",
    )
    parser.add_argument(
        "--output",
        default="docs_src/examples/repository",
        help="Directory where markdown pages should be written.",
    )
    parser.add_argument(
        "--repo-url",
        default="https://github.com/UofUEpiBio/epiworld",
        help="Base URL of the upstream repository.",
    )
    parser.add_argument(
        "--branch",
        default="master",
        help="Upstream branch name used for source links.",
    )
    return parser.parse_args()


def slugify(relative_path: str) -> str:
    sanitized = relative_path.replace("\\", "/").replace("/", "-").replace(".", "-")
    return f"{GENERATED_PAGE_PREFIX}{sanitized}".lower()


def discover_examples(source_root: Path) -> list[dict[str, str]]:
    examples: list[dict[str, str]] = []

    for filename in ROOT_SHOWCASE_FILES:
        file_path = source_root / filename
        if file_path.is_file():
            examples.append(
                {
                    "category": "Showcase files",
                    "title": filename,
                    "source_path": filename,
                }
            )

    examples_dir = source_root / "examples"
    if examples_dir.is_dir():
        for file_path in sorted(examples_dir.rglob("*")):
            if not file_path.is_file():
                continue

            if file_path.suffix not in SUPPORTED_EXTENSIONS:
                continue

            relative_path = file_path.relative_to(source_root).as_posix()
            parent = file_path.parent.relative_to(examples_dir).as_posix()
            category = "examples/" if parent == "." else f"examples/{parent}"

            examples.append(
                {
                    "category": category,
                    "title": file_path.name,
                    "source_path": relative_path,
                }
            )

    return sorted(examples, key=lambda item: item["source_path"])


def cleanup_generated_pages(output_root: Path) -> None:
    for page in output_root.glob(f"{GENERATED_PAGE_PREFIX}*.md"):
        page.unlink()


def build_page(entry: dict[str, str], source_root: Path, repo_url: str, branch: str) -> str:
    source_path = entry["source_path"]
    page_title = source_path
    file_path = source_root / source_path
    code = file_path.read_text(encoding="utf-8", errors="replace").rstrip()
    language = LANGUAGE_MAP.get(file_path.suffix, "text")
    github_url = f"{repo_url}/blob/{branch}/{source_path}"

    return "\n".join(
        [
            f"# {page_title}",
            "",
            f"- Upstream path: `{source_path}`",
            f"- Source on GitHub: [{source_path}]({github_url})",
            "",
            f"```{language}",
            code,
            "```",
            "",
        ]
    )


def build_index(
    entries: list[dict[str, str]], repo_url: str, branch: str, source_exists: bool
) -> str:
    lines = [
        "# Repository Gallery",
        "",
        "This page is generated from the upstream `epiworld` repository.",
        "",
        f"- Upstream repository: [{repo_url}]({repo_url})",
        f"- Branch used for links: `{branch}`",
    ]

    if not source_exists:
        lines.extend(
            [
                "",
                "The local `epiworld-src/` checkout was not found, so the gallery",
                "was left in placeholder mode.",
                "",
                "Run `python3 scripts/sync_examples.py --source epiworld-src` after",
                "cloning the upstream repository to populate this section.",
            ]
        )
        return "\n".join(lines) + "\n"

    if not entries:
        lines.extend(
            [
                "",
                "No supported example files were found in the upstream checkout.",
            ]
        )
        return "\n".join(lines) + "\n"

    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for entry in entries:
        grouped[entry["category"]].append(entry)

    for category in sorted(grouped):
        lines.extend(["", f"## {category}", ""])
        for entry in grouped[category]:
            slug = slugify(entry["source_path"])
            lines.append(
                f"- [{entry['title']}]({slug}.md) - `{entry['source_path']}`"
            )

    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    source_root = (repo_root / args.source).resolve()
    output_root = (repo_root / args.output).resolve()
    output_root.mkdir(parents=True, exist_ok=True)

    cleanup_generated_pages(output_root)

    source_exists = source_root.exists()
    entries = discover_examples(source_root) if source_exists else []

    for entry in entries:
        slug = slugify(entry["source_path"])
        page_path = output_root / f"{slug}.md"
        page_path.write_text(
            build_page(entry, source_root, args.repo_url, args.branch),
            encoding="utf-8",
        )

    index_path = output_root / "index.md"
    index_path.write_text(
        build_index(entries, args.repo_url, args.branch, source_exists),
        encoding="utf-8",
    )

    print(f"Synced {len(entries)} example page(s) into {output_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
