# Changelog

## [v1.0.0] — 2026-05-09

First public release of **Celine's Game Land** — a family game hub with two games, a shared profile system, and a combined leaderboard.

---

### 🏠 Celine's Game Land Hub (`celinegameland/`)

- New hub landing page (`index.html`) with animated game cards linking to both games
- Combined Python server (`server.py`) serves the hub + both games from a single port (8765)
- **Overall leaderboard** merges Food Bowl Rush wins (server-side) and Math Bond Star stars (localStorage) into one ranked table
- `start.command` launcher — double-click to start the server on macOS
- Profiles shown with emoji, color, medal icons (🥇🥈🥉), win count, and star count

---

### 🍜 Food Bowl Rush (`food-bowl-rush/`)

- **Editable custom profiles** — ✎ edit button appears only on user-created profiles (not built-in ones)
- Edit modal lets you change emoji, color, and name for any custom profile
- Profile override system persists edits in `localStorage` (`foodBowlRush_profileOverrides`)
- **🏠 Game Land** link added to the language picker screen (English version)
- **🏠 游戏中心** link added to the language picker screen (Chinese version)
- Both English (`index.html`) and Chinese (`index-chinese.html`) versions updated

---

### ⭐ Math Bond Star (`math-bond-star/`)

- **New game** built from scratch — number bond flashcard game for kids
- Four difficulty levels: Baby 🍼, Lion 🦁, Rocket 🚀, Diamond 💎
- Level select shows best star rating (1–3 ⭐) earned per level per profile
- **Hall of Fame** on the title screen — top 5 players ranked by total stars with medals
- **Shared profile system** — reads the same family profiles as Food Bowl Rush (`foodBowlRush_customProfiles` in localStorage)
- Profile select screen with full grid: built-in family members + custom profiles + ➕ Add Player
- Custom profiles show ✎ edit and ✕ delete buttons
- Scores saved in `localStorage` (`mathBondStar_scores`) — no server needed
- Sound effects: correct answer fanfare, wrong answer buzz, level complete chime, click sounds
- Animated star reveal on results screen
- Back / change-user buttons throughout the game flow

---

### Infrastructure

- Monorepo pushed to GitHub: [CelineXilingJiang/celine-game-land](https://github.com/CelineXilingJiang/celine-game-land)
- `.gitignore` excludes `scores.json`, `__pycache__`, `.DS_Store`
- All games share the same origin (`localhost:8765`) so localStorage is shared across hub and games
