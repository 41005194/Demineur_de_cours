"""
Stats and Achievements System for Minesweeper
Tracks player statistics and unlocks achievements
"""

import json
import os
from dataclasses import dataclass, asdict
from typing import Dict, List
from datetime import datetime


@dataclass
class Achievement:
    """Represents an achievement."""
    name: str
    description: str
    unlocked: bool = False
    unlock_date: str = ""
    icon: str = "🏆"  # Unicode icon


class StatsManager:
    """Manages game statistics and achievements."""

    def __init__(self, stats_file: str = "game_stats.json"):
        """
        Initialize stats manager.
        
        Args:
            stats_file: Path to stats JSON file
        """
        self.stats_file = stats_file
        self.stats = {
            "total_games": 0,
            "total_wins": 0,
            "total_losses": 0,
            "total_time_played": 0.0,
            "best_times": {},  # config -> time
            "games_by_difficulty": {"beginner": 0, "intermediate": 0, "expert": 0},
            "total_flags_placed": 0,
            "total_cells_revealed": 0,
        }
        self.achievements = self._init_achievements()
        self._load_stats()

    def _init_achievements(self) -> Dict[str, Achievement]:
        """Initialize all available achievements."""
        return {
            "first_game": Achievement(
                "First Game", "Complete your first game", False
            ),
            "ten_wins": Achievement(
                "Victory Streak", "Win 10 games", False
            ),
            "fast_beginner": Achievement(
                "Speed Runner", "Complete beginner in under 30 seconds", False
            ),
            "perfect_flag": Achievement(
                "Flag Master", "Flag all mines perfectly in a game", False
            ),
            "win_expert": Achievement(
                "Expert Solver", "Win an expert game (22x22)", False
            ),
            "hundred_games": Achievement(
                "Veteran", "Play 100 games", False
            ),
            "no_flags": Achievement(
                "Memory Master", "Win a game without using flags", False
            ),
            "speed_demon": Achievement(
                "Blitz Master", "Complete a game in under 10 seconds", False
            ),
        }

    def _load_stats(self):
        """Load stats from JSON file."""
        if os.path.exists(self.stats_file):
            try:
                with open(self.stats_file, 'r') as f:
                    data = json.load(f)
                    self.stats.update(data.get("stats", {}))
                    
                    # Load achievements
                    for ach_id, ach_data in data.get("achievements", {}).items():
                        if ach_id in self.achievements:
                            self.achievements[ach_id].unlocked = ach_data.get("unlocked", False)
                            self.achievements[ach_id].unlock_date = ach_data.get("unlock_date", "")
            except Exception as e:
                print(f"Error loading stats: {e}")

    def save_stats(self):
        """Save stats to JSON file."""
        try:
            data = {
                "stats": self.stats,
                "achievements": {
                    ach_id: {
                        "name": ach.name,
                        "description": ach.description,
                        "unlocked": ach.unlocked,
                        "unlock_date": ach.unlock_date,
                    }
                    for ach_id, ach in self.achievements.items()
                },
            }
            with open(self.stats_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving stats: {e}")

    def record_game(self, board_size: int, num_mines: int, time_taken: float, 
                    won: bool, flags_placed: int, cells_revealed: int, 
                    flags_correct: bool = False, no_flags_used: bool = False):
        """
        Record a completed game.
        
        Args:
            board_size: Size of the board (e.g., 10 for 10x10)
            num_mines: Number of mines
            time_taken: Time to complete in seconds
            won: Whether the game was won
            flags_placed: Number of flags placed
            cells_revealed: Number of cells revealed
            flags_correct: Whether all flags were placed correctly
            no_flags_used: Whether no flags were used
        """
        config = f"{board_size}x{board_size}_{num_mines}mines"
        
        # Update basic stats
        self.stats["total_games"] += 1
        self.stats["total_time_played"] += time_taken
        
        if won:
            self.stats["total_wins"] += 1
            
            # Track best time
            if config not in self.stats["best_times"] or time_taken < self.stats["best_times"][config]:
                self.stats["best_times"][config] = time_taken
        else:
            self.stats["total_losses"] += 1
        
        # Track difficulty
        if board_size == 9:
            self.stats["games_by_difficulty"]["beginner"] += 1
        elif board_size == 16:
            self.stats["games_by_difficulty"]["intermediate"] += 1
        elif board_size == 22:
            self.stats["games_by_difficulty"]["expert"] += 1
        
        self.stats["total_flags_placed"] += flags_placed
        self.stats["total_cells_revealed"] += cells_revealed
        
        # Check for achievements
        self._check_achievements(board_size, num_mines, time_taken, won, 
                                 flags_placed, flags_correct, no_flags_used)
        
        self.save_stats()

    def _check_achievements(self, board_size: int, num_mines: int, time_taken: float,
                           won: bool, flags_placed: int, flags_correct: bool, 
                           no_flags_used: bool):
        """Check and unlock achievements."""
        if won:
            # First Game
            if self.stats["total_wins"] == 1:
                self._unlock_achievement("first_game")
            
            # Ten Wins
            if self.stats["total_wins"] >= 10:
                self._unlock_achievement("ten_wins")
            
            # Speed Runner (Beginner < 30s)
            if board_size == 9 and time_taken < 30:
                self._unlock_achievement("fast_beginner")
            
            # Expert Solver
            if board_size == 22:
                self._unlock_achievement("win_expert")
            
            # Speed Demon (any game < 10s)
            if time_taken < 10:
                self._unlock_achievement("speed_demon")
            
            # Flag Master (all flags correct)
            if flags_correct and flags_placed > 0:
                self._unlock_achievement("perfect_flag")
            
            # Memory Master (no flags used)
            if no_flags_used:
                self._unlock_achievement("no_flags")
        
        # Hundred Games
        if self.stats["total_games"] >= 100:
            self._unlock_achievement("hundred_games")

    def _unlock_achievement(self, achievement_id: str):
        """Unlock an achievement."""
        if achievement_id in self.achievements:
            ach = self.achievements[achievement_id]
            if not ach.unlocked:
                ach.unlocked = True
                ach.unlock_date = datetime.now().isoformat()
                self.save_stats()
                return True
        return False

    def get_stats(self) -> Dict:
        """Get all statistics."""
        return self.stats.copy()

    def get_achievements(self) -> Dict[str, Achievement]:
        """Get all achievements."""
        return self.achievements.copy()

    def get_unlocked_count(self) -> int:
        """Get count of unlocked achievements."""
        return sum(1 for ach in self.achievements.values() if ach.unlocked)

    def get_total_count(self) -> int:
        """Get total number of achievements."""
        return len(self.achievements)

    def get_win_rate(self) -> float:
        """Get win rate percentage."""
        total = self.stats["total_games"]
        if total == 0:
            return 0.0
        return (self.stats["total_wins"] / total) * 100
