# Minesweeper v2.0 - New Features Documentation

## Overview
This is a major update to the Minesweeper game adding comprehensive game statistics, achievements, audio system, persistent settings, dark mode, and animated menus.

## New Features

### 1. 🔊 Audio System
**File**: `audio_manager.py`

Features:
- Sound effects for game events (click, flag, win, lose, reveal)
- Graceful degradation - works without pygame.mixer
- Volume control with settings persistence
- Extensible: Add custom `.wav` files to `sounds/` folder

Sound Effects:
- `click.wav` - Cell reveal sound
- `flag.wav` - Flag placement sound
- `win.wav` - Victory sound
- `lose.wav` - Defeat sound
- `reveal.wav` - Cascade reveal sound

Usage:
```python
audio_mgr.play("click")
audio_mgr.set_volume(0.7)
```

### 2. 🏆 Achievements & Statistics System
**File**: `stats_manager.py`

Features:
- 8 achievements to unlock with progressive difficulty
- Persistent statistics tracking (games, wins, losses, times)
- Win rate calculation
- Auto-achievement unlocking based on game performance
- JSON-based storage

Achievements:
1. **First Game** - Complete your first game
2. **Victory Streak** - Win 10 games
3. **Speed Runner** - Complete beginner in under 30 seconds
4. **Perfect Flag** - Flag all mines correctly in one game
5. **Expert Solver** - Win an expert game (22x22)
6. **Hundred Games** - Play 100 games
7. **Memory Master** - Win without using flags
8. **Speed Demon** - Complete any game in under 10 seconds

Statistics Tracked:
- Total games played
- Total wins/losses
- Total time played
- Best times per configuration
- Games by difficulty level
- Total flags placed
- Total cells revealed
- Achievement unlock dates

### 3. 💾 Settings Persistence
**File**: `settings_manager.py`

Features:
- Auto-saves to `game_settings.json`
- Loads settings on startup
- Persists:
  - Theme selection
  - Volume level
  - Animation speed
  - Board size and mine count
  - Dark mode setting
  - Player name
  - Window dimensions

Settings Structure:
```json
{
  "theme": "Ocean",
  "volume": 0.7,
  "animation_speed": 1.0,
  "board_size": 10,
  "num_mines": 15,
  "dark_mode": false,
  "fullscreen": false,
  "player_name": "Player",
  "window_width": 1280,
  "window_height": 720
}
```

### 4. 🌙 Dark Mode
**Implementation**: Integrated in `minesweeper.py`

Features:
- Independent toggle from theme selection
- Darkens backgrounds while maintaining readability
- Persisted in settings
- UI control in Settings menu with ON/OFF button

How it works:
- Reduces background colors by 40-60 points
- Increases text brightness by 100 points
- Maintains color harmony

### 5. 🎬 Animated Main Menu
**File**: `menu_animation.py`

Features:
- Parallax scrolling background
- Bouncing button animations with staggering
- Fade-in text effects
- Pulsing scale effects
- Smooth transitions

Classes:
- `ParallaxBackground` - Animated wave background
- `MenuAnimation` - Menu element animations
- `TextGlow` - Glowing text effects

### 6. ⚡ Auto-Reveal Feature
**Implementation**: `_check_auto_reveal()` method

Features:
- Click on a revealed numbered cell
- If all adjacent mines are flagged correctly
- All adjacent unrevealed safe cells reveal automatically
- Helps with large boards and complex sections

Conditions:
- Cell must be revealed and have adjacent mines
- Number of adjacent flags must equal adjacent mine count
- Must have unrevealed safe cells to reveal

### 7. Achievements Display
**Implementation**: `_draw_achievements()` method

Features:
- Dedicated achievements screen
- Shows all 8 achievements
- Displays unlock status and dates
- Statistics summary (games, wins, win rate)
- Pagination for scrolling through achievements

## Integration Points

### Game Loop Updates
1. Audio plays on cell click/flag/win/lose
2. Stats recorded automatically on game end
3. Settings auto-loaded on startup
4. Settings auto-saved on change

### Event Handling
- New `ACHIEVEMENTS` game state
- Dark mode toggle in settings
- Achievements navigation

### Data Files Generated
- `game_stats.json` - Statistics and achievement data
- `game_settings.json` - User preferences
- `sounds/` - Directory for audio files

## Usage Examples

### Playing a Game with New Features
1. Start game - settings load automatically
2. Toggle dark mode in Settings if desired
3. Play normally - audio plays, animations work
4. Win/lose - stats recorded, achievements checked
5. View achievements from main menu

### Accessing Statistics
- View win rate and game count on achievements screen
- Check achievement unlock dates
- Track personal best times per configuration

### Customizing Audio
1. Create `.wav` files:
   - click.wav
   - flag.wav
   - win.wav
   - lose.wav
   - reveal.wav
2. Place in `sounds/` folder
3. Game automatically loads and plays them

## JSON File Formats

### game_stats.json
```json
{
  "stats": {
    "total_games": 5,
    "total_wins": 3,
    "total_losses": 2,
    "total_time_played": 124.5,
    "best_times": {
      "10x10_15mines": 45.2
    },
    "games_by_difficulty": {
      "beginner": 2,
      "intermediate": 3,
      "expert": 0
    },
    "total_flags_placed": 45,
    "total_cells_revealed": 234
  },
  "achievements": {
    "first_game": {
      "name": "First Game",
      "description": "Complete your first game",
      "unlocked": true,
      "unlock_date": "2024-12-09T15:30:00"
    }
  }
}
```

### game_settings.json
```json
{
  "theme": "Ocean",
  "volume": 0.7,
  "animation_speed": 1.0,
  "board_size": 10,
  "num_mines": 15,
  "dark_mode": false,
  "fullscreen": false,
  "player_name": "Player",
  "window_width": 1280,
  "window_height": 720
}
```

## Technical Details

### Class Relationships
- `Minesweeper` (main) uses:
  - `AudioManager` for sound effects
  - `StatsManager` for statistics
  - `SettingsManager` for preferences
  - `ParallaxBackground` + `MenuAnimation` for UI

### Data Flow
1. Settings Manager loads on startup
2. Audio Manager initializes with loaded volume
3. Game state updates trigger event handlers
4. Stats recorded on game completion
5. All changes auto-saved to JSON files

### Performance Considerations
- Audio system handles missing files gracefully
- JSON serialization is lightweight
- Parallax background uses efficient line drawing
- Animation calculations use basic trig functions

## Future Enhancements
- Sound volume control slider in Settings
- Custom achievement definitions
- Leaderboard synchronization with stats
- Player profile system
- Multiple save slots
- Replay system with auto-reveal history

## Troubleshooting

### Audio not working?
- Check `pygame.mixer` is available
- Look for `sounds/` folder
- Check console for initialization messages

### Settings not saving?
- Ensure write permissions in game directory
- Check JSON files aren't corrupted
- Try deleting and recreating JSON files

### Achievements not unlocking?
- Requirements must be met exactly (check times, mine counts)
- JSON file must be writable
- Stats must be recorded before checking achievements

## Code Quality
- Type hints on all public methods
- Comprehensive error handling
- Graceful degradation for missing dependencies
- Clear separation of concerns
- Well-commented complex logic
