#!/usr/bin/env python3
"""Fetch public FPL classic league standings and write a static JSON snapshot."""
import json, os, urllib.request, datetime, time

LEAGUE_ID = os.environ.get("FPL_LEAGUE_ID", "1978")
BASE = "https://fantasy.premierleague.com/api"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; JinxClubFPL/1.0)"}

def get(path):
    req = urllib.request.Request(BASE + path, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))

def main():
    first = get(f"/leagues-classic/{LEAGUE_ID}/standings/?page_standings=1")
    league = first.get("league", {})
    standings = first.get("standings", {})
    results = list(standings.get("results", []))
    page = 2
    while standings.get("has_next"):
        time.sleep(0.4)
        data = get(f"/leagues-classic/{LEAGUE_ID}/standings/?page_standings={page}")
        standings = data.get("standings", {})
        results.extend(standings.get("results", []))
        page += 1
    events = get("/events/")
    current = next((e for e in events if e.get("is_current")), None)
    if current is None:
        current = next((e for e in reversed(events) if e.get("finished")), None)
    payload = {
        "league_id": int(LEAGUE_ID),
        "league_name": league.get("name", "Jinx Club Fantasy Premier League"),
        "gameweek": current.get("id") if current else None,
        "gameweek_name": current.get("name") if current else None,
        "updated_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "source": "Fantasy Premier League public API",
        "standings": results,
    }
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Wrote {len(results)} managers for league {LEAGUE_ID}")

if __name__ == "__main__":
    main()
