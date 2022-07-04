import json
import os
import sys

filename = "tilos_shows2.json"
script_folder = os.path.dirname(sys.argv[0])
SRC_FILE = os.path.join(script_folder, filename)

with open(SRC_FILE, "r") as f:
    raw = "".join(f.readlines())
    SHOWS = json.loads(raw)
