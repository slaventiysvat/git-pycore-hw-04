#!/usr/bin/env python
"""
Directory tree visualizer with colored output.

Usage:
    python git-pycore-hw-04/task3.py <path>

Notes:
    - Uses colorama for colorized output on Windows and POSIX.
    - Prints directories and files with different colors.
    - Handles common errors (missing path, not a directory, permission issues).
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Iterable, Tuple

from colorama import init as colorama_init, Fore, Style


def _list_entries(p: Path) -> Tuple[list[Path], list[Path]]:
    """Return (dirs, files) for path p, both sorted case-insensitively."""
    dirs, files = [], []
    try:
        for entry in p.iterdir():
            if entry.is_dir():
                dirs.append(entry)
            else:
                files.append(entry)
    except PermissionError:
        # If we cannot list this directory, return empty; caller will print a note.
        return [], []
    key = lambda x: x.name.lower()
    return sorted(dirs, key=key), sorted(files, key=key)


def _print_tree(base: Path, prefix: str = "") -> None:
    """Recursively print the directory tree starting at base."""
    dirs, files = _list_entries(base)
    entries: list[Tuple[Path, bool]] = [(d, True) for d in dirs] + [(f, False) for f in files]

    for idx, (entry, is_dir) in enumerate(entries):
        is_last = idx == len(entries) - 1
        connector = "└── " if is_last else "├── "

        if is_dir:
            print(prefix + connector + Fore.CYAN + Style.BRIGHT + entry.name + Style.RESET_ALL)
            # Prepare next prefix: keep vertical line if there are more siblings
            next_prefix = prefix + ("    " if is_last else "│   ")
            # Recurse
            try:
                _print_tree(entry, next_prefix)
            except PermissionError:
                print(next_prefix + Fore.RED + "[permission denied]" + Style.RESET_ALL)
        else:
            print(prefix + connector + Fore.GREEN + entry.name + Style.RESET_ALL)


def main(argv: list[str]) -> int:
    colorama_init(autoreset=True)

    if len(argv) != 2:
        print("Usage: python git-pycore-hw-06/task3.py <path>")
        return 2

    target = Path(argv[1]).expanduser().resolve()

    if not target.exists():
        print(Fore.RED + f"Error: path does not exist: {target}" + Style.RESET_ALL)
        return 1
    if not target.is_dir():
        print(Fore.RED + f"Error: not a directory: {target}" + Style.RESET_ALL)
        return 1

    # Print root
    print(Fore.BLUE + Style.BRIGHT + target.name + Style.RESET_ALL)
    try:
        _print_tree(target)
    except PermissionError:
        # Very unlikely at root level; still handle gracefully
        print(Fore.RED + "[permission denied]" + Style.RESET_ALL)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
