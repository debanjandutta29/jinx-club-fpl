# Jinx Club Fantasy Premier League website

This is a static GitHub Pages site for FPL Classic mini-league **1978**.

## What it does
- Reads the public FPL Classic League standings API.
- Shows manager, team, overall rank, total points, latest Gameweek points and rank movement.
- GitHub Actions refreshes the snapshot daily; you can also run it manually.
- The site itself is mobile responsive and needs no server or paid hosting.

## Publish it with GitHub Pages
1. Sign in to GitHub and create a **new public repository**, e.g. `jinx-club-fpl`.
2. Upload the files and folders from this package, keeping the `.github/workflows/update.yml` path.
3. In the repository, open **Settings → Pages**.
4. Under **Build and deployment**, choose **Deploy from a branch**.
5. Choose branch **main** and folder **/ (root)**, then Save.
6. Open **Actions → Update FPL standings → Run workflow** once to fetch the first data snapshot. The workflow will also run daily automatically.
7. Your site will be available at `https://YOUR-GITHUB-USERNAME.github.io/jinx-club-fpl/` after Pages finishes deploying.

## File layout
- `index.html` — website
- `update_fpl.py` — fetches all pages of FPL league data
- `.github/workflows/update.yml` — scheduled refresh
- `data.json` — generated standings snapshot

## Notes
- FPL's public API is unofficial/undocumented and may change.
- The scheduled workflow commits the updated `data.json` to the repository root, where the page reads it.
- **Important:** the page fetches `data.json` from its own root. Before first publish, move generated `public/data.json` to the repository root, or use the workflow variant below that writes root data.json.
