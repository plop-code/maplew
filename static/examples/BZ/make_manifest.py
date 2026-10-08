#!/usr/bin/env python3
"""Create manifest.json listing every file in the current directory.

Order: .csv files first, then all other files grouped by extension
(alphabetical by extension, then by file name within each group).
"""

import json
import os
import sys

OUTPUT_NAME = "manifest.json"


def sort_key(name):
    ext = os.path.splitext(name)[1].lower()
    # CSVs first (0), everything else after (1), grouped by extension, then name
    return (0 if ext == ".csv" else 1, ext, name.lower())


def main():
    here = os.getcwd()
    script_name = os.path.basename(sys.argv[0])

    files = [
        f
        for f in os.listdir(here)
        if os.path.isfile(os.path.join(here, f))
        and f not in (OUTPUT_NAME, script_name)
    ]
    files.sort(key=sort_key)

    with open(OUTPUT_NAME, "w", encoding="utf-8") as fh:
        json.dump({"files": files}, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    print(f"Wrote {len(files)} file names to {OUTPUT_NAME}")


if __name__ == "__main__":
    main()
