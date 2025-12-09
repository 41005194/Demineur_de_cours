"""
Minesweeper Game
A fully-featured Minesweeper with customization, themes, timer, and leaderboards.
"""

import pygame
import random
import time
import os
import json
import math
from datetime import datetime
from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional, Tuple, Dict

# Initialize Pygame
pygame.init()
pygame.font.init()

# Get display info
display_info = pygame.display.Info()
FULLSCREEN_WIDTH = display_info.current_w
FULLSCREEN_HEIGHT = display_info.current_h

# Default windowed mode size (80% of screen)
WINDOWED_WIDTH = int(FULLSCREEN_WIDTH * 0.8)
WINDOWED_HEIGHT = int(FULLSCREEN_HEIGHT * 0.8)

# Current screen dimensions (will be updated based on mode)
SCREEN_WIDTH = WINDOWED_WIDTH
SCREEN_HEIGHT = WINDOWED_HEIGHT

# Game constants - now relative to screen size
MIN_CELL_SIZE = max(20, int(SCREEN_HEIGHT * 0.025))
MAX_CELL_SIZE = max(40, int(SCREEN_HEIGHT * 0.06))
HEADER_HEIGHT = int(SCREEN_HEIGHT * 0.12)
MENU_WIDTH = int(SCREEN_WIDTH * 0.25)

# Animation constants
REVEAL_ANIMATION_DURATION = 0.15  # seconds
FLAG_ANIMATION_DURATION = 0.1

# Themes
THEMES = {
    "Ocean": {
        "background": (20, 30, 48),
        "header": (30, 45, 65),
        "cell_hidden": (65, 105, 225),
        "cell_hidden_hover": (100, 140, 255),
        "cell_revealed": (240, 248, 255),
        "cell_mine": (255, 99, 71),
        "cell_flag": (255, 215, 0),
        "border": (25, 55, 95),
        "text": (255, 255, 255),
        "text_dark": (30, 30, 30),
        "button": (65, 105, 225),
        "button_hover": (100, 140, 255),
        "numbers": [
            (0, 0, 0),
            (0, 0, 255),
            (0, 128, 0),
            (255, 0, 0),
            (0, 0, 128),
            (128, 0, 0),
            (0, 128, 128),
            (0, 0, 0),
            (128, 128, 128),
        ],
    },
    "Forest": {
        "background": (34, 49, 34),
        "header": (45, 65, 45),
        "cell_hidden": (76, 153, 76),
        "cell_hidden_hover": (100, 180, 100),
        "cell_revealed": (245, 245, 220),
        "cell_mine": (255, 69, 0),
        "cell_flag": (255, 165, 0),
        "border": (30, 60, 30),
        "text": (255, 255, 255),
        "text_dark": (30, 30, 30),
        "button": (76, 153, 76),
        "button_hover": (100, 180, 100),
        "numbers": [
            (0, 0, 0),
            (0, 100, 0),
            (139, 69, 19),
            (178, 34, 34),
            (72, 61, 139),
            (128, 0, 0),
            (32, 178, 170),
            (0, 0, 0),
            (128, 128, 128),
        ],
    },
    "Sunset": {
        "background": (45, 25, 35),
        "header": (65, 35, 50),
        "cell_hidden": (255, 107, 107),
        "cell_hidden_hover": (255, 140, 140),
        "cell_revealed": (255, 250, 240),
        "cell_mine": (139, 0, 0),
        "cell_flag": (255, 215, 0),
        "border": (80, 40, 60),
        "text": (255, 255, 255),
        "text_dark": (45, 25, 35),
        "button": (255, 107, 107),
        "button_hover": (255, 140, 140),
        "numbers": [
            (0, 0, 0),
            (255, 69, 0),
            (255, 140, 0),
            (220, 20, 60),
            (199, 21, 133),
            (139, 0, 139),
            (255, 20, 147),
            (0, 0, 0),
            (128, 128, 128),
        ],
    },
    "Candy": {
        "background": (255, 182, 193),
        "header": (255, 160, 180),
        "cell_hidden": (186, 85, 211),
        "cell_hidden_hover": (218, 112, 214),
        "cell_revealed": (255, 250, 250),
        "cell_mine": (220, 20, 60),
        "cell_flag": (50, 205, 50),
        "border": (255, 105, 180),
        "text": (75, 0, 130),
        "text_dark": (75, 0, 130),
        "button": (186, 85, 211),
        "button_hover": (218, 112, 214),
        "numbers": [
            (0, 0, 0),
            (138, 43, 226),
            (255, 20, 147),
            (255, 69, 0),
            (30, 144, 255),
            (255, 105, 180),
            (0, 206, 209),
            (0, 0, 0),
            (128, 128, 128),
        ],
    },
    "Midnight": {
        "background": (15, 15, 25),
        "header": (25, 25, 40),
        "cell_hidden": (60, 60, 90),
        "cell_hidden_hover": (80, 80, 120),
        "cell_revealed": (45, 45, 60),
        "cell_mine": (255, 50, 50),
        "cell_flag": (0, 255, 127),
        "border": (40, 40, 60),
        "text": (200, 200, 220),
        "text_dark": (200, 200, 220),
        "button": (60, 60, 90),
        "button_hover": (80, 80, 120),
        "numbers": [
            (150, 150, 150),
            (100, 149, 237),
            (50, 205, 50),
            (255, 99, 71),
            (138, 43, 226),
            (255, 215, 0),
            (0, 255, 255),
            (255, 255, 255),
            (169, 169, 169),
        ],
    },
    "Neon": {
        "background": (10, 10, 15),
        "header": (15, 15, 25),
        "cell_hidden": (20, 20, 35),
        "cell_hidden_hover": (30, 30, 50),
        "cell_revealed": (25, 25, 40),
        "cell_mine": (255, 0, 100),
        "cell_flag": (0, 255, 255),
        "border": (255, 0, 255),
        "text": (0, 255, 200),
        "text_dark": (0, 255, 200),
        "button": (40, 0, 80),
        "button_hover": (80, 0, 160),
        "numbers": [
            (100, 100, 100),
            (0, 200, 255),
            (0, 255, 100),
            (255, 50, 150),
            (200, 0, 255),
            (255, 255, 0),
            (255, 100, 0),
            (255, 255, 255),
            (150, 150, 150),
        ],
    },
    "Retro": {
        "background": (40, 40, 40),
        "header": (60, 60, 60),
        "cell_hidden": (100, 100, 100),
        "cell_hidden_hover": (120, 120, 120),
        "cell_revealed": (200, 200, 180),
        "cell_mine": (180, 50, 50),
        "cell_flag": (255, 200, 50),
        "border": (80, 80, 80),
        "text": (255, 255, 230),
        "text_dark": (40, 40, 40),
        "button": (100, 100, 100),
        "button_hover": (130, 130, 130),
        "numbers": [
            (60, 60, 60),
            (0, 0, 180),
            (0, 120, 0),
            (180, 0, 0),
            (0, 0, 120),
            (120, 0, 0),
            (0, 120, 120),
            (0, 0, 0),
            (100, 100, 100),
        ],
    },
    "Aurora": {
        "background": (10, 20, 40),
        "header": (15, 30, 55),
        "cell_hidden": (30, 80, 120),
        "cell_hidden_hover": (40, 100, 150),
        "cell_revealed": (220, 240, 250),
        "cell_mine": (255, 80, 120),
        "cell_flag": (150, 255, 150),
        "border": (50, 150, 200),
        "text": (200, 255, 255),
        "text_dark": (20, 40, 60),
        "button": (40, 120, 180),
        "button_hover": (60, 150, 210),
        "numbers": [
            (50, 50, 50),
            (100, 200, 255),
            (100, 255, 150),
            (255, 150, 180),
            (180, 100, 255),
            (255, 200, 100),
            (100, 255, 255),
            (50, 50, 50),
            (150, 150, 150),
        ],
    },
    "Lava": {
        "background": (30, 10, 10),
        "header": (50, 15, 15),
        "cell_hidden": (150, 50, 30),
        "cell_hidden_hover": (180, 70, 40),
        "cell_revealed": (255, 240, 220),
        "cell_mine": (50, 50, 50),
        "cell_flag": (255, 255, 100),
        "border": (100, 30, 20),
        "text": (255, 220, 180),
        "text_dark": (50, 20, 10),
        "button": (180, 60, 30),
        "button_hover": (220, 80, 40),
        "numbers": [
            (80, 40, 30),
            (255, 150, 50),
            (255, 200, 50),
            (255, 80, 80),
            (200, 100, 50),
            (150, 50, 50),
            (255, 180, 100),
            (100, 50, 30),
            (180, 150, 120),
        ],
    },
    "Ice": {
        "background": (230, 245, 255),
        "header": (200, 230, 250),
        "cell_hidden": (150, 200, 230),
        "cell_hidden_hover": (170, 215, 240),
        "cell_revealed": (255, 255, 255),
        "cell_mine": (80, 80, 100),
        "cell_flag": (255, 100, 100),
        "border": (180, 210, 235),
        "text": (40, 60, 90),
        "text_dark": (40, 60, 90),
        "button": (130, 180, 220),
        "button_hover": (150, 200, 235),
        "numbers": [
            (100, 100, 100),
            (0, 100, 200),
            (50, 150, 100),
            (200, 80, 80),
            (100, 50, 150),
            (150, 80, 80),
            (50, 150, 150),
            (50, 50, 50),
            (130, 130, 130),
        ],
    },
    "Desert": {
        "background": (60, 45, 30),
        "header": (80, 60, 40),
        "cell_hidden": (194, 154, 108),
        "cell_hidden_hover": (214, 174, 128),
        "cell_revealed": (255, 228, 181),
        "cell_mine": (80, 40, 20),
        "cell_flag": (255, 140, 0),
        "border": (139, 90, 43),
        "text": (255, 248, 220),
        "text_dark": (60, 30, 10),
        "button": (205, 133, 63),
        "button_hover": (222, 184, 135),
        "numbers": [
            (100, 70, 40),
            (210, 105, 30),
            (255, 165, 0),
            (178, 34, 34),
            (160, 82, 45),
            (139, 69, 19),
            (184, 134, 11),
            (101, 67, 33),
            (160, 120, 80),
        ],
    },
    "Galaxy": {
        "background": (15, 10, 30),
        "header": (25, 15, 45),
        "cell_hidden": (60, 40, 100),
        "cell_hidden_hover": (80, 60, 130),
        "cell_revealed": (140, 120, 180),
        "cell_mine": (255, 50, 100),
        "cell_flag": (255, 215, 0),
        "border": (100, 50, 150),
        "text": (230, 200, 255),
        "text_dark": (50, 30, 80),
        "button": (80, 50, 120),
        "button_hover": (110, 80, 150),
        "numbers": [
            (100, 80, 130),
            (138, 43, 226),
            (255, 105, 180),
            (255, 69, 0),
            (75, 0, 130),
            (199, 21, 133),
            (148, 0, 211),
            (186, 85, 211),
            (153, 102, 204),
        ],
    },
    "Matrix": {
        "background": (0, 10, 0),
        "header": (0, 20, 0),
        "cell_hidden": (0, 80, 0),
        "cell_hidden_hover": (0, 120, 0),
        "cell_revealed": (20, 50, 20),
        "cell_mine": (255, 0, 0),
        "cell_flag": (0, 255, 255),
        "border": (0, 255, 0),
        "text": (0, 255, 0),
        "text_dark": (0, 255, 0),
        "button": (0, 100, 0),
        "button_hover": (0, 150, 0),
        "numbers": [
            (0, 200, 0),
            (50, 255, 50),
            (100, 255, 100),
            (150, 255, 150),
            (0, 200, 0),
            (0, 180, 0),
            (0, 220, 0),
            (0, 240, 0),
            (80, 255, 80),
        ],
    },
    "Cherry": {
        "background": (40, 15, 20),
        "header": (60, 20, 30),
        "cell_hidden": (180, 50, 80),
        "cell_hidden_hover": (220, 70, 100),
        "cell_revealed": (255, 192, 203),
        "cell_mine": (100, 0, 20),
        "cell_flag": (255, 255, 100),
        "border": (139, 0, 50),
        "text": (255, 240, 245),
        "text_dark": (80, 20, 40),
        "button": (200, 60, 90),
        "button_hover": (230, 90, 120),
        "numbers": [
            (150, 60, 80),
            (255, 20, 147),
            (220, 20, 60),
            (178, 34, 34),
            (199, 21, 133),
            (219, 112, 147),
            (255, 105, 180),
            (205, 92, 92),
            (176, 48, 96),
        ],
    },
    "Emerald": {
        "background": (10, 30, 20),
        "header": (15, 45, 30),
        "cell_hidden": (46, 125, 50),
        "cell_hidden_hover": (60, 150, 65),
        "cell_revealed": (144, 238, 144),
        "cell_mine": (139, 0, 0),
        "cell_flag": (255, 215, 0),
        "border": (34, 139, 34),
        "text": (240, 255, 240),
        "text_dark": (20, 60, 30),
        "button": (60, 179, 113),
        "button_hover": (90, 200, 140),
        "numbers": [
            (40, 100, 50),
            (0, 128, 0),
            (34, 139, 34),
            (0, 100, 0),
            (50, 205, 50),
            (60, 179, 113),
            (32, 178, 170),
            (46, 139, 87),
            (85, 170, 100),
        ],
    },
    "Copper": {
        "background": (25, 20, 15),
        "header": (40, 30, 20),
        "cell_hidden": (120, 80, 50),
        "cell_hidden_hover": (150, 100, 60),
        "cell_revealed": (218, 165, 105),
        "cell_mine": (50, 30, 20),
        "cell_flag": (0, 206, 209),
        "border": (139, 90, 43),
        "text": (255, 235, 205),
        "text_dark": (40, 25, 15),
        "button": (160, 110, 70),
        "button_hover": (180, 130, 90),
        "numbers": [
            (100, 70, 40),
            (184, 134, 11),
            (218, 165, 32),
            (205, 127, 50),
            (160, 82, 45),
            (139, 69, 19),
            (210, 105, 30),
            (160, 100, 50),
            (180, 140, 90),
        ],
    },
    "Lavender": {
        "background": (45, 35, 60),
        "header": (60, 45, 80),
        "cell_hidden": (147, 112, 219),
        "cell_hidden_hover": (167, 132, 239),
        "cell_revealed": (230, 230, 250),
        "cell_mine": (75, 0, 130),
        "cell_flag": (255, 215, 0),
        "border": (123, 104, 238),
        "text": (248, 248, 255),
        "text_dark": (60, 40, 90),
        "button": (138, 43, 226),
        "button_hover": (158, 63, 246),
        "numbers": [
            (100, 70, 140),
            (138, 43, 226),
            (147, 112, 219),
            (153, 50, 204),
            (186, 85, 211),
            (216, 191, 216),
            (221, 160, 221),
            (218, 112, 214),
            (200, 150, 220),
        ],
    },
    "Cyber": {
        "background": (5, 5, 15),
        "header": (10, 10, 25),
        "cell_hidden": (30, 30, 60),
        "cell_hidden_hover": (50, 50, 90),
        "cell_revealed": (60, 60, 100),
        "cell_mine": (255, 0, 0),
        "cell_flag": (0, 255, 255),
        "border": (0, 255, 255),
        "text": (0, 255, 255),
        "text_dark": (0, 255, 255),
        "button": (50, 50, 100),
        "button_hover": (70, 70, 130),
        "numbers": [
            (100, 200, 255),
            (0, 255, 255),
            (255, 0, 255),
            (255, 100, 255),
            (100, 255, 255),
            (200, 100, 255),
            (255, 255, 100),
            (150, 150, 255),
            (200, 200, 255),
        ],
    },
    "Jungle": {
        "background": (20, 35, 20),
        "header": (30, 50, 30),
        "cell_hidden": (34, 139, 34),
        "cell_hidden_hover": (50, 170, 50),
        "cell_revealed": (154, 205, 50),
        "cell_mine": (101, 67, 33),
        "cell_flag": (255, 140, 0),
        "border": (85, 107, 47),
        "text": (240, 255, 240),
        "text_dark": (25, 50, 25),
        "button": (107, 142, 35),
        "button_hover": (124, 160, 50),
        "numbers": [
            (50, 80, 30),
            (0, 128, 0),
            (34, 139, 34),
            (107, 142, 35),
            (85, 107, 47),
            (124, 252, 0),
            (127, 255, 0),
            (173, 255, 47),
            (144, 238, 144),
        ],
    },
    "Slate": {
        "background": (30, 35, 40),
        "header": (45, 52, 60),
        "cell_hidden": (70, 80, 90),
        "cell_hidden_hover": (90, 100, 110),
        "cell_revealed": (176, 196, 222),
        "cell_mine": (25, 25, 112),
        "cell_flag": (255, 165, 0),
        "border": (112, 128, 144),
        "text": (240, 248, 255),
        "text_dark": (30, 40, 50),
        "button": (100, 120, 140),
        "button_hover": (120, 140, 160),
        "numbers": [
            (60, 70, 80),
            (70, 130, 180),
            (100, 149, 237),
            (65, 105, 225),
            (72, 61, 139),
            (106, 90, 205),
            (123, 104, 238),
            (135, 206, 250),
            (140, 160, 180),
        ],
    },
}


class GameState(Enum):
    MENU = 1
    PLAYING = 2
    WON = 3
    LOST = 4
    LEADERBOARD = 5
    SETTINGS = 6


@dataclass
class Cell:
    is_mine: bool = False
    is_revealed: bool = False
    is_flagged: bool = False
    adjacent_mines: int = 0
    # Animation state
    reveal_time: float = 0.0
    flag_time: float = 0.0
    animation_active: bool = False


@dataclass
class CellAnimation:
    """Tracks animation state for a cell"""

    start_time: float
    duration: float
    animation_type: str  # 'reveal', 'flag', 'unflag', 'explode'


@dataclass
class LeaderboardEntry:
    name: str
    time: float
    date: str
    board_size: int
    mines: int


class Button:
    def __init__(self, x: int, y: int, width: int, height: int, text: str, font_size: int = 24):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.hovered = False

    def draw(self, screen: pygame.Surface, theme: dict):
        color = theme["button_hover"] if self.hovered else theme["button"]
        pygame.draw.rect(screen, color, self.rect, border_radius=10)
        pygame.draw.rect(screen, theme["border"], self.rect, 2, border_radius=10)

        text_surface = self.font.render(self.text, True, theme["text"])
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event: pygame.event.Event) -> bool:
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False


class Slider:
    def __init__(self, x: int, y: int, width: int, min_val: int, max_val: int, current: int, label: str):
        self.rect = pygame.Rect(x, y, width, 30)
        self.min_val = min_val
        self.max_val = max_val
        self.value = current
        self.label = label
        self.dragging = False
        self.font = pygame.font.Font(None, 24)

    def draw(self, screen: pygame.Surface, theme: dict):
        # Label
        label_surface = self.font.render(f"{self.label}: {self.value}", True, theme["text"])
        screen.blit(label_surface, (self.rect.x, self.rect.y - 25))

        # Track
        track_rect = pygame.Rect(self.rect.x, self.rect.y + 10, self.rect.width, 10)
        pygame.draw.rect(screen, theme["border"], track_rect, border_radius=5)

        # Filled portion
        fill_width = int((self.value - self.min_val) / (self.max_val - self.min_val) * self.rect.width)
        fill_rect = pygame.Rect(self.rect.x, self.rect.y + 10, fill_width, 10)
        pygame.draw.rect(screen, theme["button"], fill_rect, border_radius=5)

        # Handle
        handle_x = self.rect.x + fill_width
        pygame.draw.circle(screen, theme["button_hover"], (handle_x, self.rect.y + 15), 12)
        pygame.draw.circle(screen, theme["text"], (handle_x, self.rect.y + 15), 12, 2)

    def handle_event(self, event: pygame.event.Event) -> bool:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            handle_x = self.rect.x + int((self.value - self.min_val) / (self.max_val - self.min_val) * self.rect.width)
            handle_rect = pygame.Rect(handle_x - 12, self.rect.y + 3, 24, 24)
            if handle_rect.collidepoint(event.pos) or self.rect.collidepoint(event.pos):
                self.dragging = True
                self._update_value(event.pos[0])
                return True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            self._update_value(event.pos[0])
            return True
        return False

    def _update_value(self, mouse_x: int):
        rel_x = max(0, min(mouse_x - self.rect.x, self.rect.width))
        self.value = int(self.min_val + (rel_x / self.rect.width) * (self.max_val - self.min_val))


class Minesweeper:
    def __init__(self):
        # Start in windowed mode
        self.is_fullscreen = False
        self.screen = pygame.display.set_mode((WINDOWED_WIDTH, WINDOWED_HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Minesweeper")
        self.clock = pygame.time.Clock()

        # Update global screen dimensions
        global SCREEN_WIDTH, SCREEN_HEIGHT, MIN_CELL_SIZE, MAX_CELL_SIZE, HEADER_HEIGHT
        SCREEN_WIDTH = WINDOWED_WIDTH
        SCREEN_HEIGHT = WINDOWED_HEIGHT
        MIN_CELL_SIZE = max(20, int(SCREEN_HEIGHT * 0.025))
        MAX_CELL_SIZE = max(40, int(SCREEN_HEIGHT * 0.06))
        HEADER_HEIGHT = int(SCREEN_HEIGHT * 0.12)

        # Game settings
        self.board_size = 10
        self.num_mines = 15
        self.current_theme = "Ocean"

        # Game state
        self.state = GameState.MENU
        self.board: List[List[Cell]] = []
        self.start_time: Optional[float] = None
        self.elapsed_time: float = 0
        self.first_click = True
        self.cells_revealed = 0
        self.flags_placed = 0

        # Animation tracking
        self.animations: Dict[Tuple[int, int], CellAnimation] = {}
        self.current_time = time.time()

        # Player info
        self.player_name = "Player"
        self.name_input_active = False

        # Leaderboard data directory
        self.data_dir = os.path.dirname(os.path.abspath(__file__))
        self.leaderboard_dir = os.path.join(self.data_dir, "leaderboards")
        os.makedirs(self.leaderboard_dir, exist_ok=True)

        # UI elements
        self._setup_ui()

        # Fonts - scaled to screen size
        self._setup_fonts()

    def _setup_fonts(self):
        """Setup fonts based on current screen size."""
        current_height = self.screen.get_height()
        base_size = int(current_height / 15)
        self.title_font = pygame.font.Font(None, int(base_size * 1.5))
        self.header_font = pygame.font.Font(None, base_size)
        self.text_font = pygame.font.Font(None, int(base_size * 0.7))
        self.cell_font = pygame.font.Font(None, int(base_size * 0.75))
        self.small_font = pygame.font.Font(None, int(base_size * 0.5))

    def _toggle_fullscreen(self):
        """Toggle between fullscreen and windowed mode."""
        self.is_fullscreen = not self.is_fullscreen
        if self.is_fullscreen:
            self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(self.windowed_size, pygame.RESIZABLE)
        self._setup_fonts()
        self._setup_ui()

    def _setup_ui(self):
        # Get current screen dimensions (works for both windowed and fullscreen)
        current_width = self.screen.get_width()
        current_height = self.screen.get_height()

        center_x = current_width // 2
        btn_width = int(current_width * 0.18)
        btn_height = int(current_height * 0.055)
        small_btn_height = int(current_height * 0.04)
        font_size = int(current_height * 0.03)
        small_font_size = int(current_height * 0.022)

        # Menu buttons - positioned relative to screen with better spacing
        menu_start_y = int(current_height * 0.28)
        menu_spacing = int(current_height * 0.09)
        fullscreen_text = "Exit Fullscreen" if self.is_fullscreen else "Enter Fullscreen"
        self.menu_buttons = {
            "play": Button(center_x - btn_width // 2, menu_start_y, btn_width, btn_height, "Play", font_size),
            "leaderboard": Button(
                center_x - btn_width // 2, menu_start_y + menu_spacing, btn_width, btn_height, "Leaderboard", font_size
            ),
            "settings": Button(
                center_x - btn_width // 2, menu_start_y + menu_spacing * 2, btn_width, btn_height, "Settings", font_size
            ),
            "fullscreen": Button(
                center_x - btn_width // 2,
                menu_start_y + menu_spacing * 3,
                btn_width,
                small_btn_height,
                fullscreen_text,
                small_font_size,
            ),
            "quit": Button(center_x - btn_width // 2, menu_start_y + menu_spacing * 4, btn_width, btn_height, "Quit", font_size),
        }

        # Settings sliders - repositioned
        slider_width = int(current_width * 0.25)
        self.size_slider = Slider(
            center_x - slider_width // 2, int(current_height * 0.28), slider_width, 5, 25, self.board_size, "Board Size"
        )
        self.mines_slider = Slider(
            center_x - slider_width // 2, int(current_height * 0.35), slider_width, 5, 200, self.num_mines, "Number of Mines"
        )

        # Settings buttons - repositioned
        preset_btn_width = int(current_width * 0.12)
        preset_y = int(current_height * 0.47)
        self.settings_buttons = {
            "back": Button(center_x - btn_width // 2, int(current_height * 0.87), btn_width, btn_height, "Back to Menu", font_size),
            "beginner": Button(
                center_x - int(preset_btn_width * 1.7),
                preset_y,
                preset_btn_width,
                small_btn_height,
                "Beginner (9x9)",
                small_font_size,
            ),
            "intermediate": Button(
                center_x - preset_btn_width // 2,
                preset_y,
                preset_btn_width,
                small_btn_height,
                "Intermediate (16x16)",
                small_font_size,
            ),
            "expert": Button(
                center_x + int(preset_btn_width * 0.7),
                preset_y,
                preset_btn_width,
                small_btn_height,
                "Expert (22x22)",
                small_font_size,
            ),
        }

        # Theme buttons - arranged in a scrollable grid with better layout
        self.theme_buttons = {}
        theme_names = list(THEMES.keys())
        theme_btn_width = int(current_width * 0.09)
        theme_btn_height = int(current_height * 0.035)
        themes_per_row = 4
        theme_start_x = center_x - (themes_per_row * theme_btn_width + (themes_per_row - 1) * 10) // 2
        theme_start_y = int(current_height * 0.55)

        for i, name in enumerate(theme_names):
            row = i // themes_per_row
            col = i % themes_per_row
            x = theme_start_x + col * (theme_btn_width + 10)
            y = theme_start_y + row * (theme_btn_height + 8)
            self.theme_buttons[name] = Button(x, y, theme_btn_width, theme_btn_height, name, small_font_size)

        # Game buttons
        game_btn_width = int(current_width * 0.08)
        game_btn_height = int(current_height * 0.045)
        self.game_buttons = {
            "menu": Button(
                int(current_width * 0.02), int(current_height * 0.02), game_btn_width, game_btn_height, "Menu", small_font_size
            ),
            "restart": Button(
                int(current_width * 0.02) + game_btn_width + 10,
                int(current_height * 0.02),
                game_btn_width,
                game_btn_height,
                "Restart",
                small_font_size,
            ),
        }

        # Leaderboard buttons
        self.lb_buttons = {
            "back": Button(
                center_x - btn_width // 2,
                current_height - int(current_height * 0.12),
                btn_width,
                btn_height,
                "Back to Menu",
                font_size,
            ),
            "clear": Button(
                center_x - btn_width // 2,
                current_height - int(current_height * 0.19),
                btn_width,
                small_btn_height,
                "Clear Leaderboard",
                small_font_size,
            ),
            "prev": Button(
                center_x - int(current_width * 0.18),
                int(current_height * 0.18),
                int(current_width * 0.08),
                small_btn_height,
                "< Prev",
                small_font_size,
            ),
            "next": Button(
                center_x + int(current_width * 0.1),
                int(current_height * 0.18),
                int(current_width * 0.08),
                small_btn_height,
                "Next >",
                small_font_size,
            ),
        }
        self.current_lb_index = 0

        # Win/Lose buttons
        end_btn_width = int(current_width * 0.15)
        self.end_buttons = {
            "menu": Button(
                center_x - end_btn_width - 10, int(current_height * 0.45), end_btn_width, btn_height, "Main Menu", font_size
            ),
            "restart": Button(center_x + 10, int(current_height * 0.45), end_btn_width, btn_height, "Play Again", font_size),
        }

        # Name input rect
        self.name_input_rect = pygame.Rect(center_x - btn_width // 2, int(current_height * 0.22), btn_width, small_btn_height)

    def _get_theme(self) -> dict:
        return THEMES[self.current_theme]

    def _toggle_fullscreen(self):
        """Toggle between fullscreen and windowed mode."""
        global SCREEN_WIDTH, SCREEN_HEIGHT, MIN_CELL_SIZE, MAX_CELL_SIZE, HEADER_HEIGHT

        self.is_fullscreen = not self.is_fullscreen

        if self.is_fullscreen:
            self.screen = pygame.display.set_mode((FULLSCREEN_WIDTH, FULLSCREEN_HEIGHT), pygame.FULLSCREEN)
            SCREEN_WIDTH = FULLSCREEN_WIDTH
            SCREEN_HEIGHT = FULLSCREEN_HEIGHT
        else:
            self.screen = pygame.display.set_mode((WINDOWED_WIDTH, WINDOWED_HEIGHT), pygame.RESIZABLE)
            SCREEN_WIDTH = WINDOWED_WIDTH
            SCREEN_HEIGHT = WINDOWED_HEIGHT

        # Update size-dependent constants
        MIN_CELL_SIZE = max(20, int(SCREEN_HEIGHT * 0.025))
        MAX_CELL_SIZE = max(40, int(SCREEN_HEIGHT * 0.06))
        HEADER_HEIGHT = int(SCREEN_HEIGHT * 0.12)

        # Recreate UI elements and fonts for new size
        self._setup_ui()
        base_size = int(SCREEN_HEIGHT / 15)
        self.title_font = pygame.font.Font(None, int(base_size * 1.5))
        self.header_font = pygame.font.Font(None, base_size)
        self.text_font = pygame.font.Font(None, int(base_size * 0.7))
        self.cell_font = pygame.font.Font(None, int(base_size * 0.75))
        self.small_font = pygame.font.Font(None, int(base_size * 0.5))

    def _get_leaderboard_file(self, size: int, mines: int) -> str:
        return os.path.join(self.leaderboard_dir, f"leaderboard_{size}x{size}_{mines}mines.txt")

    def _get_all_leaderboard_configs(self) -> List[Tuple[int, int]]:
        """Get all leaderboard configurations that exist."""
        configs = []
        if os.path.exists(self.leaderboard_dir):
            for filename in os.listdir(self.leaderboard_dir):
                if filename.startswith("leaderboard_") and filename.endswith(".txt"):
                    try:
                        parts = filename[12:-4].split("_")
                        size = int(parts[0].split("x")[0])
                        mines = int(parts[1].replace("mines", ""))
                        configs.append((size, mines))
                    except:
                        pass
        # Add current config if not exists
        if (self.board_size, self.num_mines) not in configs:
            configs.append((self.board_size, self.num_mines))
        configs.sort()
        return configs

    def _load_leaderboard(self, size: int, mines: int) -> List[LeaderboardEntry]:
        filepath = self._get_leaderboard_file(size, mines)
        entries = []
        if os.path.exists(filepath):
            try:
                with open(filepath, "r") as f:
                    for line in f:
                        parts = line.strip().split("|")
                        if len(parts) >= 5:
                            entries.append(
                                LeaderboardEntry(
                                    name=parts[0],
                                    time=float(parts[1]),
                                    date=parts[2],
                                    board_size=int(parts[3]),
                                    mines=int(parts[4]),
                                )
                            )
            except:
                pass
        return sorted(entries, key=lambda x: x.time)[:10]

    def _save_leaderboard(self, entries: List[LeaderboardEntry], size: int, mines: int):
        filepath = self._get_leaderboard_file(size, mines)
        with open(filepath, "w") as f:
            for entry in entries[:10]:
                f.write(f"{entry.name}|{entry.time:.2f}|{entry.date}|{entry.board_size}|{entry.mines}\n")

    def _add_to_leaderboard(self, time: float):
        entry = LeaderboardEntry(
            name=self.player_name,
            time=time,
            date=datetime.now().strftime("%Y-%m-%d %H:%M"),
            board_size=self.board_size,
            mines=self.num_mines,
        )
        entries = self._load_leaderboard(self.board_size, self.num_mines)
        entries.append(entry)
        entries = sorted(entries, key=lambda x: x.time)[:10]
        self._save_leaderboard(entries, self.board_size, self.num_mines)

    def _clear_current_leaderboard(self):
        configs = self._get_all_leaderboard_configs()
        if configs and self.current_lb_index < len(configs):
            size, mines = configs[self.current_lb_index]
            filepath = self._get_leaderboard_file(size, mines)
            if os.path.exists(filepath):
                os.remove(filepath)

    def _create_board(self):
        self.board = [[Cell() for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.first_click = True
        self.cells_revealed = 0
        self.flags_placed = 0
        self.start_time = None
        self.elapsed_time = 0
        self.animations.clear()

    def _place_mines(self, exclude_x: int, exclude_y: int):
        """Place mines, excluding the first clicked cell and its neighbors."""
        excluded = set()
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                nx, ny = exclude_x + dx, exclude_y + dy
                if 0 <= nx < self.board_size and 0 <= ny < self.board_size:
                    excluded.add((nx, ny))

        available = [(x, y) for x in range(self.board_size) for y in range(self.board_size) if (x, y) not in excluded]

        # Ensure we don't place more mines than available cells
        actual_mines = min(self.num_mines, len(available))
        mine_positions = random.sample(available, actual_mines)

        for x, y in mine_positions:
            self.board[y][x].is_mine = True

        # Calculate adjacent mines
        for y in range(self.board_size):
            for x in range(self.board_size):
                if not self.board[y][x].is_mine:
                    count = 0
                    for dy in range(-1, 2):
                        for dx in range(-1, 2):
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < self.board_size and 0 <= ny < self.board_size:
                                if self.board[ny][nx].is_mine:
                                    count += 1
                    self.board[y][x].adjacent_mines = count

    def _reveal_cell(self, x: int, y: int, delay: float = 0):
        if not (0 <= x < self.board_size and 0 <= y < self.board_size):
            return

        cell = self.board[y][x]
        if cell.is_revealed or cell.is_flagged:
            return

        cell.is_revealed = True
        cell.reveal_time = self.current_time + delay
        self.cells_revealed += 1

        # Add reveal animation
        self.animations[(x, y)] = CellAnimation(
            start_time=self.current_time + delay,
            duration=REVEAL_ANIMATION_DURATION,
            animation_type="explode" if cell.is_mine else "reveal",
        )

        if cell.is_mine:
            self.state = GameState.LOST
            self._reveal_all_mines()
            return

        # Check win condition
        total_non_mines = self.board_size * self.board_size - self.num_mines
        if self.cells_revealed >= total_non_mines:
            self.state = GameState.WON
            self.elapsed_time = time.time() - self.start_time
            self._add_to_leaderboard(self.elapsed_time)
            return

        # Flood fill for empty cells with cascading delay
        if cell.adjacent_mines == 0:
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if dx != 0 or dy != 0:
                        self._reveal_cell(x + dx, y + dy, delay + 0.03)

    def _reveal_all_mines(self):
        delay = 0
        for y in range(self.board_size):
            for x in range(self.board_size):
                if self.board[y][x].is_mine and not self.board[y][x].is_revealed:
                    self.board[y][x].is_revealed = True
                    self.board[y][x].reveal_time = self.current_time + delay
                    self.animations[(x, y)] = CellAnimation(
                        start_time=self.current_time + delay, duration=REVEAL_ANIMATION_DURATION * 1.5, animation_type="explode"
                    )
                    delay += 0.05

    def _toggle_flag(self, x: int, y: int):
        if not (0 <= x < self.board_size and 0 <= y < self.board_size):
            return

        cell = self.board[y][x]
        if cell.is_revealed:
            return

        if cell.is_flagged:
            cell.is_flagged = False
            cell.flag_time = self.current_time
            self.flags_placed -= 1
            self.animations[(x, y)] = CellAnimation(
                start_time=self.current_time, duration=FLAG_ANIMATION_DURATION, animation_type="unflag"
            )
        else:
            cell.is_flagged = True
            cell.flag_time = self.current_time
            self.flags_placed += 1
            self.animations[(x, y)] = CellAnimation(
                start_time=self.current_time, duration=FLAG_ANIMATION_DURATION, animation_type="flag"
            )

    def _calculate_board_dimensions(self) -> Tuple[int, int, int, int]:
        """Calculate board position and cell size to fit the screen."""
        current_width = self.screen.get_width()
        current_height = self.screen.get_height()
        current_header_height = int(current_height * 0.12)

        available_width = current_width - 40
        available_height = current_height - current_header_height - 40

        cell_size = min(available_width // self.board_size, available_height // self.board_size)
        cell_size = max(MIN_CELL_SIZE, min(MAX_CELL_SIZE, cell_size))

        board_width = cell_size * self.board_size
        board_height = cell_size * self.board_size

        board_x = (current_width - board_width) // 2
        board_y = current_header_height + (available_height - board_height) // 2

        return board_x, board_y, cell_size, board_width

    def _get_cell_from_pos(self, pos: Tuple[int, int]) -> Optional[Tuple[int, int]]:
        """Convert mouse position to cell coordinates."""
        board_x, board_y, cell_size, _ = self._calculate_board_dimensions()

        x = (pos[0] - board_x) // cell_size
        y = (pos[1] - board_y) // cell_size

        if 0 <= x < self.board_size and 0 <= y < self.board_size:
            return x, y
        return None

    def _draw_cell(self, x: int, y: int, board_x: int, board_y: int, cell_size: int, mouse_pos: Tuple[int, int]):
        cell = self.board[y][x]

        base_rect = pygame.Rect(board_x + x * cell_size, board_y + y * cell_size, cell_size - 2, cell_size - 2)

        # Get animation state
        anim = self.animations.get((x, y))
        anim_progress = 1.0
        if anim and self.current_time < anim.start_time + anim.duration:
            elapsed = self.current_time - anim.start_time
            if elapsed < 0:
                anim_progress = 0.0
            else:
                anim_progress = min(1.0, elapsed / anim.duration)

        # Calculate animated rect for reveal animation
        rect = base_rect.copy()
        if anim and anim.animation_type == "reveal" and anim_progress < 1.0:
            # Scale animation - cell grows from center
            scale = 0.5 + 0.5 * self._ease_out_back(anim_progress)
            new_size = int((cell_size - 2) * scale)
            rect = pygame.Rect(0, 0, new_size, new_size)
            rect.center = base_rect.center

        # Determine cell color
        color = self._get_cell_color(cell, rect, mouse_pos, anim, anim_progress)

        # Draw cell background with potential glow for explosions
        if anim and anim.animation_type == "explode" and anim_progress < 1.0:
            glow_size = int(cell_size * (1 + 0.3 * math.sin(anim_progress * math.pi)))
            glow_rect = pygame.Rect(0, 0, glow_size, glow_size)
            glow_rect.center = base_rect.center
            glow_color = (255, 200, 100, int(150 * (1 - anim_progress)))
            glow_surface = pygame.Surface((glow_size, glow_size), pygame.SRCALPHA)
            pygame.draw.rect(glow_surface, glow_color, glow_surface.get_rect(), border_radius=6)
            self.screen.blit(glow_surface, glow_rect)

        pygame.draw.rect(self.screen, color, rect, border_radius=4)

        # Draw cell content
        self._draw_cell_content(cell, rect, cell_size, anim, anim_progress)

    def _get_cell_color(
        self, cell: Cell, rect: pygame.Rect, mouse_pos: Tuple[int, int], anim: Optional[CellAnimation], anim_progress: float
    ) -> Tuple[int, int, int]:
        """Determine the color for a cell based on its state and animation."""
        theme = self._get_theme()

        if cell.is_revealed:
            if cell.is_mine:
                # Animate mine color
                if anim and anim.animation_type == "explode" and anim_progress < 1.0:
                    t = self._ease_out_quad(anim_progress)
                    return self._lerp_color((255, 255, 200), theme["cell_mine"], t)
                return theme["cell_mine"]
            else:
                # Animate reveal color
                if anim and anim.animation_type == "reveal" and anim_progress < 1.0:
                    t = self._ease_out_quad(anim_progress)
                    return self._lerp_color(theme["cell_hidden"], theme["cell_revealed"], t)
                return theme["cell_revealed"]
        else:
            if rect.collidepoint(mouse_pos) and self.state == GameState.PLAYING:
                return theme["cell_hidden_hover"]
            return theme["cell_hidden"]

    def _draw_cell_content(
        self, cell: Cell, rect: pygame.Rect, cell_size: int, anim: Optional[CellAnimation], anim_progress: float
    ):
        """Draw the content of a cell (number, mine, or flag)."""
        if cell.is_revealed:
            if cell.is_mine:
                self._draw_mine(rect, cell_size, anim_progress if anim and anim.animation_type == "explode" else 1.0)
            elif cell.adjacent_mines > 0:
                self._draw_number(rect, cell.adjacent_mines, anim_progress if anim else 1.0)
        elif cell.is_flagged:
            flag_scale = 1.0
            if anim and anim.animation_type == "flag" and anim_progress < 1.0:
                flag_scale = self._ease_out_back(anim_progress)
            self._draw_flag(rect, cell_size, flag_scale)

    def _draw_mine(self, rect: pygame.Rect, cell_size: int, progress: float):
        """Draw a mine with animation."""
        center = rect.center
        scale = 0.8 + 0.2 * progress

        # Main circle
        radius = int(cell_size // 4 * scale)
        pygame.draw.circle(self.screen, (0, 0, 0), center, radius)
        pygame.draw.circle(self.screen, (50, 50, 50), center, int(radius * 0.6))

        # Spikes with rotation animation
        rotation_offset = (1 - progress) * 45
        for angle in range(0, 360, 45):
            actual_angle = angle + rotation_offset
            end_x = center[0] + int(math.cos(math.radians(actual_angle)) * cell_size // 3 * scale)
            end_y = center[1] + int(math.sin(math.radians(actual_angle)) * cell_size // 3 * scale)
            pygame.draw.line(self.screen, (0, 0, 0), center, (end_x, end_y), 2)

    def _draw_number(self, rect: pygame.Rect, number: int, progress: float):
        """Draw a number with fade-in animation."""
        theme = self._get_theme()
        num_color = theme["numbers"][number]

        num_surface = self.cell_font.render(str(number), True, num_color)

        # Scale effect
        if progress < 1.0:
            scale = 0.5 + 0.5 * self._ease_out_back(progress)
            new_size = (int(num_surface.get_width() * scale), int(num_surface.get_height() * scale))
            if new_size[0] > 0 and new_size[1] > 0:
                num_surface = pygame.transform.scale(num_surface, new_size)

        num_rect = num_surface.get_rect(center=rect.center)
        self.screen.blit(num_surface, num_rect)

    def _draw_flag(self, rect: pygame.Rect, cell_size: int, scale: float):
        """Draw a flag with scale animation."""
        theme = self._get_theme()
        center = rect.center
        flag_color = theme["cell_flag"]

        # Pole
        pole_height = int(cell_size // 2 * scale)
        pygame.draw.line(
            self.screen, (100, 100, 100), (center[0], center[1] + pole_height // 2), (center[0], center[1] - pole_height // 2), 2
        )

        # Flag triangle
        flag_size = int(cell_size // 4 * scale)
        points = [
            (center[0], center[1] - pole_height // 2),
            (center[0] + flag_size, center[1] - pole_height // 2 + flag_size // 2),
            (center[0], center[1] - pole_height // 2 + flag_size),
        ]
        pygame.draw.polygon(self.screen, flag_color, points)

    # Animation easing functions
    def _ease_out_quad(self, t: float) -> float:
        return 1 - (1 - t) * (1 - t)

    def _ease_out_back(self, t: float) -> float:
        c1 = 1.70158
        c3 = c1 + 1
        return 1 + c3 * pow(t - 1, 3) + c1 * pow(t - 1, 2)

    def _lerp_color(self, c1: Tuple[int, int, int], c2: Tuple[int, int, int], t: float) -> Tuple[int, int, int]:
        """Linear interpolation between two colors."""
        return (int(c1[0] + (c2[0] - c1[0]) * t), int(c1[1] + (c2[1] - c1[1]) * t), int(c1[2] + (c2[2] - c1[2]) * t))

    def _draw_menu(self):
        theme = self._get_theme()
        current_width = self.screen.get_width()
        current_height = self.screen.get_height()

        self.screen.fill(theme["background"])

        # Title - positioned at top
        title = self.title_font.render("MINESWEEPER", True, theme["text"])
        title_rect = title.get_rect(center=(current_width // 2, int(current_height * 0.10)))
        self.screen.blit(title, title_rect)

        # Subtitle
        subtitle = self.text_font.render("A classic puzzle game", True, theme["text"])
        subtitle_rect = subtitle.get_rect(center=(current_width // 2, int(current_height * 0.16)))
        self.screen.blit(subtitle, subtitle_rect)

        # Draw buttons
        for button in self.menu_buttons.values():
            button.draw(self.screen, theme)

        # Draw player name input section - positioned at bottom
        name_section_y = int(current_height * 0.78)
        name_label = self.text_font.render("Player Name:", True, theme["text"])
        name_label_rect = name_label.get_rect(center=(current_width // 2, name_section_y))
        self.screen.blit(name_label, name_label_rect)

        name_input_rect = pygame.Rect(
            current_width // 2 - int(current_width * 0.08),
            name_section_y + int(current_height * 0.03),
            int(current_width * 0.16),
            int(current_height * 0.04),
        )
        input_color = theme["button_hover"] if self.name_input_active else theme["button"]
        pygame.draw.rect(self.screen, input_color, name_input_rect, border_radius=5)
        pygame.draw.rect(self.screen, theme["border"], name_input_rect, 2, border_radius=5)
        self.name_input_rect = name_input_rect

        name_surface = self.text_font.render(self.player_name, True, theme["text"])
        name_text_rect = name_surface.get_rect(center=name_input_rect.center)
        self.screen.blit(name_surface, name_text_rect)

        # Current settings display - at the very bottom
        settings_y = int(current_height * 0.90)
        settings_line1 = self.small_font.render(
            f"Board: {self.board_size}x{self.board_size} | Mines: {self.num_mines} | Theme: {self.current_theme}",
            True,
            theme["text"],
        )
        settings1_rect = settings_line1.get_rect(center=(current_width // 2, settings_y))
        self.screen.blit(settings_line1, settings1_rect)

        mode_text = "Fullscreen" if self.is_fullscreen else "Windowed"
        settings_line2 = self.small_font.render(f"Display Mode: {mode_text} | Press F11 to toggle", True, theme["text"])
        settings2_rect = settings_line2.get_rect(center=(current_width // 2, settings_y + int(current_height * 0.04)))
        self.screen.blit(settings_line2, settings2_rect)

    def _draw_settings(self):
        theme = self._get_theme()
        current_width = self.screen.get_width()
        current_height = self.screen.get_height()

        self.screen.fill(theme["background"])

        # Title
        title = self.header_font.render("Settings", True, theme["text"])
        title_rect = title.get_rect(center=(current_width // 2, int(current_height * 0.08)))
        self.screen.blit(title, title_rect)

        # Player name input - at the top
        name_label = self.text_font.render("Player Name:", True, theme["text"])
        name_label_rect = name_label.get_rect(center=(current_width // 2, int(current_height * 0.14)))
        self.screen.blit(name_label, name_label_rect)

        input_color = theme["button_hover"] if self.name_input_active else theme["button"]
        name_rect = pygame.Rect(
            current_width // 2 - int(current_width * 0.08),
            int(current_height * 0.18),
            int(current_width * 0.16),
            int(current_height * 0.04),
        )
        pygame.draw.rect(self.screen, input_color, name_rect, border_radius=5)
        pygame.draw.rect(self.screen, theme["border"], name_rect, 2, border_radius=5)
        self.name_input_rect = name_rect

        name_surface = self.text_font.render(self.player_name, True, theme["text"])
        name_text_rect = name_surface.get_rect(center=name_rect.center)
        self.screen.blit(name_surface, name_text_rect)

        # Sliders section
        slider_label = self.text_font.render("Board Configuration", True, theme["text"])
        slider_label_rect = slider_label.get_rect(center=(current_width // 2, int(current_height * 0.25)))
        self.screen.blit(slider_label, slider_label_rect)

        self.size_slider.draw(self.screen, theme)
        self.mines_slider.draw(self.screen, theme)

        # Update mines slider max based on board size
        max_mines = (self.size_slider.value**2) - 9
        self.mines_slider.max_val = max(10, max_mines)
        if self.mines_slider.value > self.mines_slider.max_val:
            self.mines_slider.value = self.mines_slider.max_val

        # Preset buttons section
        preset_label = self.text_font.render("Quick Presets", True, theme["text"])
        preset_label_rect = preset_label.get_rect(center=(current_width // 2, int(current_height * 0.43)))
        self.screen.blit(preset_label, preset_label_rect)

        for button_name, button in self.settings_buttons.items():
            if button_name != "back":
                button.draw(self.screen, theme)

        # Theme selection section - with current theme highlighted
        theme_label = self.text_font.render(f"Theme: {self.current_theme}", True, theme["text"])
        theme_label_rect = theme_label.get_rect(center=(current_width // 2, int(current_height * 0.52)))
        self.screen.blit(theme_label, theme_label_rect)

        # Draw theme buttons in a grid
        for name, button in self.theme_buttons.items():
            # Highlight current theme with a border
            if name == self.current_theme:
                highlight_rect = button.rect.inflate(4, 4)
                pygame.draw.rect(self.screen, theme["cell_flag"], highlight_rect, 3, border_radius=8)
            button.draw(self.screen, theme)

        # Back button at the bottom
        self.settings_buttons["back"].draw(self.screen, theme)

        # Help text at bottom
        help_text = self.small_font.render(
            "Click theme buttons to preview | Use sliders or presets to configure board", True, theme["text"]
        )
        help_rect = help_text.get_rect(center=(current_width // 2, current_height - int(current_height * 0.03)))
        self.screen.blit(help_text, help_rect)

    def _draw_game(self):
        theme = self._get_theme()
        current_width = self.screen.get_width()
        current_height = self.screen.get_height()
        current_header_height = int(current_height * 0.12)
        mouse_pos = pygame.mouse.get_pos()

        self.screen.fill(theme["background"])

        # Header background
        pygame.draw.rect(self.screen, theme["header"], (0, 0, current_width, current_header_height - 10))

        # Draw game buttons
        for button in self.game_buttons.values():
            button.draw(self.screen, theme)

        # Timer
        if self.state == GameState.PLAYING and self.start_time:
            current_time = time.time() - self.start_time
        else:
            current_time = self.elapsed_time

        time_text = self.header_font.render(f"Time: {current_time:.1f}s", True, theme["text"])
        self.screen.blit(time_text, (SCREEN_WIDTH // 2 - int(SCREEN_WIDTH * 0.06), int(SCREEN_HEIGHT * 0.03)))

        # Mines counter
        remaining = self.num_mines - self.flags_placed
        mines_text = self.header_font.render(f"Mines: {remaining}", True, theme["text"])
        self.screen.blit(mines_text, (SCREEN_WIDTH - int(SCREEN_WIDTH * 0.14), int(SCREEN_HEIGHT * 0.03)))

        # Board info
        info_text = self.small_font.render(f"{self.board_size}x{self.board_size} • {self.num_mines} mines", True, theme["text"])
        self.screen.blit(info_text, (SCREEN_WIDTH // 2 - int(SCREEN_WIDTH * 0.05), int(SCREEN_HEIGHT * 0.08)))

        # Draw board
        board_x, board_y, cell_size, _ = self._calculate_board_dimensions()

        for y in range(self.board_size):
            for x in range(self.board_size):
                self._draw_cell(x, y, board_x, board_y, cell_size, mouse_pos)

    def _draw_end_screen(self):
        theme = self._get_theme()

        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.screen.blit(overlay, (0, 0))

        # Result box
        box_width = int(SCREEN_WIDTH * 0.35)
        box_height = int(SCREEN_HEIGHT * 0.4)
        box_rect = pygame.Rect(SCREEN_WIDTH // 2 - box_width // 2, int(SCREEN_HEIGHT * 0.18), box_width, box_height)
        pygame.draw.rect(self.screen, theme["header"], box_rect, border_radius=20)
        pygame.draw.rect(self.screen, theme["border"], box_rect, 3, border_radius=20)

        # Title
        if self.state == GameState.WON:
            title = self.header_font.render("*** YOU WON! ***", True, (50, 205, 50))
            time_text = self.text_font.render(f"Time: {self.elapsed_time:.2f} seconds", True, theme["text"])
        else:
            title = self.header_font.render("*** GAME OVER ***", True, (255, 99, 71))
            time_text = self.text_font.render("Better luck next time!", True, theme["text"])

        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, int(SCREEN_HEIGHT * 0.25)))
        self.screen.blit(title, title_rect)

        time_rect = time_text.get_rect(center=(SCREEN_WIDTH // 2, int(SCREEN_HEIGHT * 0.33)))
        self.screen.blit(time_text, time_rect)

        # Stats
        stats_text = self.small_font.render(
            f"Board: {self.board_size}x{self.board_size} | Mines: {self.num_mines}", True, theme["text"]
        )
        stats_rect = stats_text.get_rect(center=(SCREEN_WIDTH // 2, int(SCREEN_HEIGHT * 0.38)))
        self.screen.blit(stats_text, stats_rect)

        # Buttons
        for button in self.end_buttons.values():
            button.draw(self.screen, theme)

    def _draw_leaderboard(self):
        theme = self._get_theme()
        current_width = self.screen.get_width()
        current_height = self.screen.get_height()

        self.screen.fill(theme["background"])

        # Title
        title = self.header_font.render("Leaderboard", True, theme["text"])
        title_rect = title.get_rect(center=(current_width // 2, int(current_height * 0.08)))
        self.screen.blit(title, title_rect)

        configs = self._get_all_leaderboard_configs()
        if not configs:
            no_data = self.text_font.render("No leaderboard data yet!", True, theme["text"])
            no_data_rect = no_data.get_rect(center=(current_width // 2, current_height // 2))
            self.screen.blit(no_data, no_data_rect)
        else:
            self._draw_leaderboard_content(configs, theme)

        # Buttons
        self.lb_buttons["back"].draw(self.screen, theme)
        self.lb_buttons["clear"].draw(self.screen, theme)

    def _draw_leaderboard_content(self, configs: List[Tuple[int, int]], theme: dict):
        """Draw the leaderboard content when there are entries."""
        current_width = self.screen.get_width()
        current_height = self.screen.get_height()

        # Ensure index is valid
        self.current_lb_index = max(0, min(self.current_lb_index, len(configs) - 1))
        size, mines = configs[self.current_lb_index]

        # Config selector
        config_text = self.text_font.render(f"{size}x{size} - {mines} mines", True, theme["text"])
        config_rect = config_text.get_rect(center=(current_width // 2, int(current_height * 0.15)))
        self.screen.blit(config_text, config_rect)

        # Navigation buttons
        if len(configs) > 1:
            self.lb_buttons["prev"].draw(self.screen, theme)
            self.lb_buttons["next"].draw(self.screen, theme)

        # Page indicator
        page_text = self.small_font.render(f"{self.current_lb_index + 1} / {len(configs)}", True, theme["text"])
        page_rect = page_text.get_rect(center=(current_width // 2, int(current_height * 0.22)))
        self.screen.blit(page_text, page_rect)

        # Leaderboard entries
        entries = self._load_leaderboard(size, mines)

        # Table header
        header_y = int(current_height * 0.28)
        headers = ["Rank", "Name", "Time", "Date"]
        positions = [
            current_width // 2 - int(current_width * 0.2),
            current_width // 2 - int(current_width * 0.08),
            current_width // 2 + int(current_width * 0.04),
            current_width // 2 + int(current_width * 0.14),
        ]

        for header, pos in zip(headers, positions):
            header_surface = self.text_font.render(header, True, theme["text"])
            self.screen.blit(header_surface, (pos, header_y))

        self._draw_leaderboard_entries(entries, header_y, positions, theme)

    def _draw_leaderboard_entries(self, entries: List[LeaderboardEntry], header_y: int, positions: List[int], theme: dict):
        """Draw individual leaderboard entries."""
        current_width = self.screen.get_width()
        current_height = self.screen.get_height()
        row_height = int(current_height * 0.04)

        if entries:
            for i, entry in enumerate(entries):
                y = header_y + 40 + i * row_height
                color = theme["cell_flag"] if i < 3 else theme["text"]

                rank_text = self.text_font.render(f"#{i + 1}", True, color)
                name_text = self.text_font.render(entry.name[:12], True, color)
                time_text = self.text_font.render(f"{entry.time:.2f}s", True, color)
                date_text = self.small_font.render(entry.date, True, color)

                self.screen.blit(rank_text, (positions[0], y))
                self.screen.blit(name_text, (positions[1], y))
                self.screen.blit(time_text, (positions[2], y))
                self.screen.blit(date_text, (positions[3], y))
        else:
            no_entries = self.text_font.render("No entries yet for this configuration", True, theme["text"])
            no_entries_rect = no_entries.get_rect(center=(current_width // 2, int(current_height * 0.4)))
            self.screen.blit(no_entries, no_entries_rect)

    def _handle_menu_events(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.name_input_rect.collidepoint(event.pos):
                self.name_input_active = True
            else:
                self.name_input_active = False

        if event.type == pygame.KEYDOWN and self.name_input_active:
            if event.key == pygame.K_BACKSPACE:
                self.player_name = self.player_name[:-1]
            elif event.key == pygame.K_RETURN:
                self.name_input_active = False
            elif len(self.player_name) < 12 and event.unicode.isprintable():
                self.player_name += event.unicode
            return

        # Handle F11 key for fullscreen toggle
        if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            self._toggle_fullscreen()
            return

        if self.menu_buttons["play"].handle_event(event):
            self._create_board()
            self.state = GameState.PLAYING
        elif self.menu_buttons["leaderboard"].handle_event(event):
            self.state = GameState.LEADERBOARD
        elif self.menu_buttons["settings"].handle_event(event):
            self.state = GameState.SETTINGS
        elif self.menu_buttons["fullscreen"].handle_event(event):
            self._toggle_fullscreen()
        elif self.menu_buttons["quit"].handle_event(event):
            pygame.quit()
            exit()

    def _handle_settings_events(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.name_input_rect.collidepoint(event.pos):
                self.name_input_active = True
            else:
                self.name_input_active = False

        if event.type == pygame.KEYDOWN and self.name_input_active:
            if event.key == pygame.K_BACKSPACE:
                self.player_name = self.player_name[:-1]
            elif event.key == pygame.K_RETURN:
                self.name_input_active = False
            elif len(self.player_name) < 12 and event.unicode.isprintable():
                self.player_name += event.unicode
            return

        self.size_slider.handle_event(event)
        self.mines_slider.handle_event(event)

        self.board_size = self.size_slider.value
        self.num_mines = self.mines_slider.value

        if self.settings_buttons["back"].handle_event(event):
            self.state = GameState.MENU
        elif self.settings_buttons["beginner"].handle_event(event):
            self.size_slider.value = 9
            self.mines_slider.value = 10
            self.board_size = 9
            self.num_mines = 10
        elif self.settings_buttons["intermediate"].handle_event(event):
            self.size_slider.value = 16
            self.mines_slider.value = 40
            self.board_size = 16
            self.num_mines = 40
        elif self.settings_buttons["expert"].handle_event(event):
            self.size_slider.value = 22
            self.mines_slider.value = 99
            self.board_size = 22
            self.num_mines = 99

        for name, button in self.theme_buttons.items():
            if button.handle_event(event):
                self.current_theme = name

    def _handle_game_events(self, event: pygame.event.Event):
        if self.game_buttons["menu"].handle_event(event):
            self.state = GameState.MENU
            return
        elif self.game_buttons["restart"].handle_event(event):
            self._create_board()
            return

        if event.type == pygame.MOUSEBUTTONDOWN:
            cell_pos = self._get_cell_from_pos(event.pos)
            if cell_pos:
                x, y = cell_pos
                if event.button == 1:  # Left click
                    if self.first_click:
                        self._place_mines(x, y)
                        self.first_click = False
                        self.start_time = time.time()
                    self._reveal_cell(x, y)
                elif event.button == 3:  # Right click
                    if not self.first_click:
                        self._toggle_flag(x, y)

    def _handle_end_events(self, event: pygame.event.Event):
        if self.end_buttons["menu"].handle_event(event):
            self.state = GameState.MENU
        elif self.end_buttons["restart"].handle_event(event):
            self._create_board()
            self.state = GameState.PLAYING

    def _handle_leaderboard_events(self, event: pygame.event.Event):
        configs = self._get_all_leaderboard_configs()

        if self.lb_buttons["back"].handle_event(event):
            self.state = GameState.MENU
        elif self.lb_buttons["clear"].handle_event(event):
            self._clear_current_leaderboard()
        elif self.lb_buttons["prev"].handle_event(event) and configs:
            self.current_lb_index = (self.current_lb_index - 1) % len(configs)
        elif self.lb_buttons["next"].handle_event(event) and configs:
            self.current_lb_index = (self.current_lb_index + 1) % len(configs)

    def run(self):
        running = True

        while running:
            self.current_time = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.state == GameState.MENU:
                            running = False
                        else:
                            self.state = GameState.MENU
                    elif event.key == pygame.K_F11:
                        self._toggle_fullscreen()
                elif event.type == pygame.VIDEORESIZE:
                    # Handle window resize in windowed mode
                    if not self.is_fullscreen:
                        self.windowed_size = (event.w, event.h)
                        self._setup_fonts()
                        self._setup_ui()

                # Handle events based on state
                self._dispatch_event(event)

            # Draw based on state
            self._draw_current_state()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def _dispatch_event(self, event: pygame.event.Event):
        """Dispatch event to appropriate handler based on game state."""
        if self.state == GameState.MENU:
            self._handle_menu_events(event)
        elif self.state == GameState.SETTINGS:
            self._handle_settings_events(event)
        elif self.state == GameState.PLAYING:
            self._handle_game_events(event)
        elif self.state in (GameState.WON, GameState.LOST):
            self._handle_end_events(event)
        elif self.state == GameState.LEADERBOARD:
            self._handle_leaderboard_events(event)

    def _draw_current_state(self):
        """Draw the current game state."""
        if self.state == GameState.MENU:
            self._draw_menu()
        elif self.state == GameState.SETTINGS:
            self._draw_settings()
        elif self.state == GameState.PLAYING:
            self._draw_game()
        elif self.state in (GameState.WON, GameState.LOST):
            self._draw_game()
            self._draw_end_screen()
        elif self.state == GameState.LEADERBOARD:
            self._draw_leaderboard()


if __name__ == "__main__":
    game = Minesweeper()
    game.run()
