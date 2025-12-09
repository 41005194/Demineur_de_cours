"""
Menu Animation System for Minesweeper
Provides animated menu with parallax background
"""

import math
import time
from typing import Tuple


class ParallaxBackground:
    """Animated parallax background for menu."""

    def __init__(self, width: int, height: int):
        """
        Initialize parallax background.
        
        Args:
            width: Screen width
            height: Screen height
        """
        self.width = width
        self.height = height
        self.time = 0.0
        self.speed = 0.5  # Background scroll speed

    def update(self, dt: float):
        """Update background animation."""
        self.time += dt
        self.time = self.time % (2 * math.pi)  # Loop animation

    def draw(self, screen, theme: dict):
        """Draw parallax background with waves/gradient."""
        # Base gradient background
        for y in range(self.height):
            # Interpolate between two colors
            progress = y / self.height
            r = int(theme["background"][0] * (1 - progress) + 
                   theme["header"][0] * progress)
            g = int(theme["background"][1] * (1 - progress) + 
                   theme["header"][1] * progress)
            b = int(theme["background"][2] * (1 - progress) + 
                   theme["header"][2] * progress)
            
            import pygame
            pygame.draw.line(screen, (r, g, b), (0, y), (self.width, y))
        
        # Draw animated waves overlay
        wave_height = int(self.height * 0.15)
        for x in range(self.width):
            y_offset = int(wave_height * math.sin(
                x * 0.01 + self.time * self.speed
            ))
            y = self.height // 3 + y_offset
            
            # Draw wave particles
            color = theme["cell_hidden"]
            alpha = int(50 * (0.5 + 0.5 * math.sin(self.time * 2)))
            
            # Simple dot to represent wave
            if y >= 0 and y < self.height:
                import pygame
                pygame.draw.circle(screen, color, (x, y), 1)


class MenuAnimation:
    """Handles menu element animations."""

    def __init__(self):
        """Initialize menu animations."""
        self.element_positions = {}  # Store animated positions
        self.start_time = time.time()
        self.animation_duration = 0.8  # Duration in seconds

    def update(self):
        """Update all animations."""
        elapsed = time.time() - self.start_time

    def get_bounce_offset(self, base_y: int, element_id: str, index: int = 0) -> Tuple[int, int]:
        """
        Get bouncing offset for menu element.
        
        Args:
            base_y: Base Y position
            element_id: Element identifier
            index: Element index for staggering
            
        Returns:
            (x, y) offset tuple
        """
        elapsed = time.time() - self.start_time
        # Stagger animation based on index
        delay = index * 0.1
        
        if elapsed < delay:
            return 0, 0
        
        # Bounce animation
        t = (elapsed - delay) % 1.0
        bounce = int(10 * math.sin(t * math.pi) * (1 - t))
        
        return 0, bounce

    def get_fade_alpha(self, element_id: str) -> float:
        """
        Get fade-in alpha for element.
        
        Args:
            element_id: Element identifier
            
        Returns:
            Alpha value (0.0 to 1.0)
        """
        elapsed = time.time() - self.start_time
        return min(1.0, elapsed / self.animation_duration)

    def get_pulse_scale(self, element_id: str) -> float:
        """
        Get pulsing scale for element.
        
        Args:
            element_id: Element identifier
            
        Returns:
            Scale factor (0.95 to 1.05)
        """
        elapsed = time.time() - self.start_time
        pulse = 0.95 + 0.05 * (0.5 + 0.5 * math.sin(elapsed * math.pi * 2))
        return pulse

    def reset(self):
        """Reset animation timer."""
        self.start_time = time.time()


class TextGlow:
    """Animated glowing text effect."""

    def __init__(self, base_color: Tuple[int, int, int]):
        """
        Initialize text glow.
        
        Args:
            base_color: Base RGB color
        """
        self.base_color = base_color
        self.start_time = time.time()

    def get_color(self) -> Tuple[int, int, int]:
        """Get current glowing color."""
        elapsed = time.time() - self.start_time
        glow = 0.5 + 0.5 * math.sin(elapsed * math.pi * 2)
        
        r = int(self.base_color[0] + (255 - self.base_color[0]) * glow * 0.3)
        g = int(self.base_color[1] + (255 - self.base_color[1]) * glow * 0.3)
        b = int(self.base_color[2] + (255 - self.base_color[2]) * glow * 0.3)
        
        return (min(255, r), min(255, g), min(255, b))
