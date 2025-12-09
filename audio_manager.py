"""
Audio Manager for Minesweeper Game
Handles sound effects with fallback support (no crash if pygame.mixer unavailable)
"""

import os
from typing import Dict, Optional


class AudioManager:
    """Manages game audio with graceful degradation."""

    def __init__(self, volume: float = 0.7):
        """
        Initialize audio manager.
        
        Args:
            volume: Master volume level (0.0 to 1.0)
        """
        self.volume = max(0.0, min(1.0, volume))
        self.sounds: Dict[str, Optional[object]] = {
            "click": None,
            "flag": None,
            "win": None,
            "lose": None,
            "reveal": None,
        }
        self.audio_available = False
        
        # Try to initialize pygame mixer
        try:
            import pygame
            pygame.mixer.init()
            self.audio_available = True
            self._load_sounds()
        except Exception as e:
            print(f"Audio unavailable: {e}")

    def _load_sounds(self):
        """Load sound files (create placeholder if files don't exist)."""
        if not self.audio_available:
            return

        sound_dir = os.path.join(os.path.dirname(__file__), "sounds")
        os.makedirs(sound_dir, exist_ok=True)

        # We won't actually create audio files - just prepare structure
        # In a real app, add .wav files to sounds/ directory
        self.sound_files = {
            "click": os.path.join(sound_dir, "click.wav"),
            "flag": os.path.join(sound_dir, "flag.wav"),
            "win": os.path.join(sound_dir, "win.wav"),
            "lose": os.path.join(sound_dir, "lose.wav"),
            "reveal": os.path.join(sound_dir, "reveal.wav"),
        }

        # Load sounds if files exist
        try:
            import pygame
            for sound_name, file_path in self.sound_files.items():
                if os.path.exists(file_path):
                    self.sounds[sound_name] = pygame.mixer.Sound(file_path)
                    if self.sounds[sound_name]:
                        self.sounds[sound_name].set_volume(self.volume)
        except Exception as e:
            print(f"Error loading sounds: {e}")

    def set_volume(self, volume: float):
        """Set master volume level."""
        self.volume = max(0.0, min(1.0, volume))
        
        if not self.audio_available:
            return
            
        try:
            import pygame
            pygame.mixer.music.set_volume(self.volume)
            for sound in self.sounds.values():
                if sound is not None:
                    sound.set_volume(self.volume)
        except Exception:
            pass

    def play(self, sound_name: str):
        """Play a sound effect."""
        if not self.audio_available or self.volume == 0:
            return

        try:
            sound = self.sounds.get(sound_name)
            if sound is not None:
                sound.play()
        except Exception:
            pass

    def get_volume(self) -> float:
        """Get current volume level."""
        return self.volume
