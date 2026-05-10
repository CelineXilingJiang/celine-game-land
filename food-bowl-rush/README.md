# 🍽️ Food Bowl Rush / 🥢 美食大冲关

A family food racing game built by Tao & Celine. Pick your food fighter, choose a track, and race to the bowl!

## How to Play

1. Double-click `start-game.command` to launch
2. Choose language: 🇺🇸 English or 🇨🇳 中文
3. Select number of players (1v1, 2v2, 3v3, or vs CPU)
4. Choose a track
5. Pick your family profile
6. Pick your food fighter
7. Press your key on every turn — first to the bowl wins!

**Controls:** Each player is assigned a key at the start of the game.

---

## Changelog

### 2026-03-20

**Family Profiles — Grandpa, Grandma & Add Player**
- Added 爷爷 (👴) and 奶奶 (👵) as built-in family profiles
- New ➕ Add Player card at the bottom of the profile grid — tap to open a modal
- Modal lets you type a name, pick an emoji from a grid, and choose a color swatch
- Custom profiles are saved to localStorage and survive game restarts
- Custom profiles show a small ✕ button so you can remove them any time
- Profile grid expanded to 3 columns to fit the larger roster
- Hall of Fame leaderboard now handles any number of profiles (medals never run out)
- All changes mirrored in the Chinese version (modal UI in Chinese: 添加玩家 / 取消 / 保存)

---

### 2026-03-20

**Camera & Audio Recording**
- Game automatically requests camera + microphone when a round starts
- Live mirrored preview shown in the bottom-right corner during gameplay with a blinking 🔴 REC indicator
- Minimize button (`_`) to shrink the preview out of the way
- Recording stops when the winner screen appears
- "📹 Save Video" button on the winner screen downloads the session as a `.webm` file named `food-bowl-rush_YYYYMMDD_HHMM.webm`
- Chinese version saves as `美食大冲关_YYYYMMDD_HHMM.webm`
- Silently skips recording if camera is denied or unavailable

---

### 2026-03-18

**Language Selection Screen**
- Both `index.html` and `index-chinese.html` now open with a language picker (🇺🇸 / 🇨🇳) as the very first screen
- Grandma can tap 中文 right away before anything else appears in English
- Choosing a language navigates to the correct version; you can switch at any time

**Chinese Version — 美食大冲关！**
- Full Chinese-language edition in `index-chinese.html`
- Red & gold color theme instead of blue-purple
- 12 Chinese foods: 🦐虾, 🍜面条, 🍚米饭, 🥡外卖, 🍡汤圆, 🫖茶, 🥮月饼, 🍱便当, 🥬青菜, 🥟饺子, 🫕火锅, 🍢串串
- Chinese track names: 长城大道, 东海浪涛, 泰山险道, 龙形弯道, 折返小径, 功夫云霄, 圆满争碗
- All UI text in Chinese (menus, countdown "冲啊！！！", winner screen, leaderboard 名人堂)
- Same game mechanics, profiles, and shared score file as the English version

---

### 2026-03-15

**1 Player vs CPU Mode**
- New "🤖 vs CPU" option on the player count screen
- Three difficulty levels: 😊 Easy, 😤 Medium, 🔥 Hard
- CPU auto-plays with randomised timing based on difficulty
- CPU picks a random food from whatever's left after the human player chooses

---

### 2026-03-12

**Parental Controls**
- Optional game limit per session: 1, 2, 3, 4, or 5 games (or unlimited)
- Session lock screen appears when limit is reached
- Parent unlock requires answering 3 trivia questions correctly
- New questions are drawn randomly each time
- Settings button on the title screen to adjust the limit

**Circle Rush Track Fix**
- Fixed Circle Rush track so Team A races the top arc and Team B the bottom arc
- Both teams now have equal-length paths

**Win Effects**
- Winner lane glows gold continuously until the screen changes
- "🥇 WINNER!" message replaces the key chip on win

---

### 2026-03-10

**Track Selection**
- Added 6 unique tracks to choose from before each race
- Straight track: Highway
- Curved tracks: Ocean Wave, Mountain Pass, Snake Road, Zigzag Trail, Rollercoaster
- Foods follow the curve of the track during gameplay and replay
- Track selection screen shows an animated preview of each path

**Family Profiles & Leaderboard**
- 4 family profiles: Celine 👧, Eileen 👩, Tao 👨, Kunyan 🧑
- Win tracking per profile saved across sessions
- Hall of Fame leaderboard shown on the title screen
- Reset scores button to clear the leaderboard

**File-Based Score Storage**
- Scores saved to `scores.json` via local Python server
- Scores persist across game restarts (no longer lost on refresh)
- Fallback to localStorage when server is offline

**Countdown & Game Flow**
- 5-second countdown with sound effects before each race
- "GAME START!" announcement with visual effects
- Removed overshoot rule — first food to reach the bowl wins

**Replay System**
- Full replay after every game
- Speed controls: 1x, 2x, 3x
- Sound effects included in replay
- Replay accurately follows the original path and timing

**Server & Launcher**
- `server.py` — local Python HTTP server (port 8765)
- `start-game.command` — double-click to launch on macOS

---

### 2026-03-09

**Initial Release — Food Bowl Rush v1**
- 12 food fighters, each with a unique jump trait:
  Crab, Ramen, Sweet Potato, Taco, Pizza, Sushi, Donut, Burger, Corndog, Dumpling, Ice Cream, Boba
- 1v1, 2v2, and 3v3 game modes
- Jump sound effects using Web Audio API (procedurally generated, no audio files)
- Win animation with dance effect
- "How We Built It" PDF documentation for sharing with the family
- Single-file game (HTML + CSS + JS, no frameworks)

---

## Files

| File | Description |
|------|-------------|
| `index.html` | English game (opens with language picker) |
| `index-chinese.html` | Chinese version — 美食大冲关！|
| `server.py` | Local server for score persistence |
| `start-game.command` | macOS double-click launcher |
| `scores.json` | Saved family scores (shared across both versions) |
| `how-we-built-it.pdf` | PDF doc showing how the game was made |

---

Built with love by Tao & Celine, powered by Claude Code.
