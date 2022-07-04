"""Refreshes the shows JSON file with actual API data."""
import json
import requests

res = requests.get("https://tilos.hu/api/show")
src = json.loads(res.text)

with open("tilos_shows2.json", "w") as f:
    shows = {}

    for show in src:
        shows[show["alias"]] = show

    json_shows = json.dumps(shows)
    f.write(json_shows)
