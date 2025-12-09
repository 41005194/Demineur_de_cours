"""
Settings Manager for Minesweeper
Persists game settings across sessions
"""

import json
import os
from typing import Dict, Any


class SettingsManager:
    """Manages game settings with persistence."""

    def __init__(self, settings_file: str = "game_settings.json"):
        """
        Initialize settings manager.
        
        Args:
            settings_file: Path to settings JSON file
        """
        self.settings_file = settings_file
        self.settings: Dict[str, Any] = {
            "theme": "Ocean",
            "volume": 0.7,
            "animation_speed": 1.0,
            "board_size": 10,
            "num_mines": 15,
            "dark_mode": False,
            "fullscreen": False,
            "player_name": "Player",
            "window_width": 1280,
            "window_height": 720,
        }
        self._load_settings()

    def _load_settings(self):
        """Load settings from JSON file."""
        if os.path.exists(self.settings_file):
            try:
                with open(self.settings_file, 'r') as f:
                    data = json.load(f)
                    # Update with loaded values, keeping defaults for missing keys
                    self.settings.update(data)
            except Exception as e:
                print(f"Error loading settings: {e}")

    def save_settings(self):
        """Save settings to JSON file."""
        try:
            with open(self.settings_file, 'w') as f:
                json.dump(self.settings, f, indent=2)
        except Exception as e:
            print(f"Error saving settings: {e}")

    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a setting value.
        
        Args:
            key: Setting key
            default: Default value if key doesn't exist
            
        Returns:
            Setting value or default
        """
        return self.settings.get(key, default)

    def set(self, key: str, value: Any) -> bool:
        """
        Set a setting value.
        
        Args:
            key: Setting key
            value: New value
            
        Returns:
            True if successful
        """
        try:
            self.settings[key] = value
            self.save_settings()
            return True
        except Exception as e:
            print(f"Error setting {key}: {e}")
            return False

    def get_all(self) -> Dict[str, Any]:
        """Get all settings."""
        return self.settings.copy()

    def reset_to_defaults(self):
        """Reset all settings to defaults."""
        default_settings = {
            "theme": "Ocean",
            "volume": 0.7,
            "animation_speed": 1.0,
            "board_size": 10,
            "num_mines": 15,
            "dark_mode": False,
            "fullscreen": False,
            "player_name": "Player",
            "window_width": 1280,
            "window_height": 720,
        }
        self.settings = default_settings
        self.save_settings()
