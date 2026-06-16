#!/usr/bin/env python3
"""
Clean Obsidian markdown for Hugo import.
Removes Obsidian-specific syntax and cleans the file.

Usage:
  python3 clean_obsidian.py /path/to/file.md

Output:
  /path/to/file.cleaned.md
"""

import sys
import re
from pathlib import Path

def clean_obsidian_markdown(text):
    """Remove Obsidian-specific syntax and clean markdown."""

    # Remove Obsidian comments (%%...%%)
    text = re.sub(r'%%.*?%%', '', text, flags=re.DOTALL)

    # Convert Obsidian links [[...]] to plain text (keep the label)
    # [[path/to/file]] → file
    # [[path/to/file|Label]] → Label
    def convert_link(m):
        content = m.group(1)
        if '|' in content:
            return content.split('|')[1].strip()
        else:
            # Extract filename without path
            return content.split('/')[-1].strip()

    text = re.sub(r'\[\[([^\]]+)\]\]', convert_link, text)

    # Remove Obsidian-specific emoji shortcodes (e.g., `fas:QuoteLeft`)
    text = re.sub(r'`[a-z]+:[A-Za-z]+`', '', text)

    # Remove inline Obsidian syntax like `fas:icon`
    text = re.sub(r'(?<!\w)[a-z]+:[A-Z][a-zA-Z]*(?!\w)', '', text)

    # Clean up extra whitespace (multiple blank lines → single blank line)
    text = re.sub(r'\n\n\n+', '\n\n', text)

    # Remove trailing whitespace on lines
    lines = [line.rstrip() for line in text.split('\n')]
    text = '\n'.join(lines)

    return text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 clean_obsidian.py /path/to/file.md")
        sys.exit(1)

    input_path = Path(sys.argv[1])

    if not input_path.exists():
        print(f"Error: File not found: {input_path}")
        sys.exit(1)

    # Read the file
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Clean it
    cleaned = clean_obsidian_markdown(content)

    # Write output with .cleaned.md suffix
    output_path = input_path.parent / f"{input_path.stem}.cleaned.md"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(cleaned)

    print(f"✓ Cleaned: {output_path}")
    print(f"  Original: {input_path.stat().st_size} bytes")
    print(f"  Cleaned:  {output_path.stat().st_size} bytes")

if __name__ == '__main__':
    main()
