"""
Theme definitions for Minesweeper
Contains all color schemes and visual themes
"""

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
            (0, 0, 0),        # 0 - not used
            (0, 0, 255),      # 1 - blue
            (0, 128, 0),      # 2 - green
            (255, 0, 0),      # 3 - red
            (0, 0, 128),      # 4 - dark blue
            (128, 0, 0),      # 5 - dark red
            (0, 128, 128),    # 6 - teal
            (64, 64, 64),     # 7 - dark gray
            (128, 128, 128),  # 8 - gray
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
            (0, 0, 0),        # 0 - not used
            (0, 100, 0),      # 1 - dark green
            (139, 69, 19),    # 2 - brown
            (178, 34, 34),    # 3 - firebrick
            (72, 61, 139),    # 4 - dark slate blue
            (128, 0, 0),      # 5 - maroon
            (32, 178, 170),   # 6 - light sea green
            (184, 134, 11),   # 7 - dark goldenrod
            (105, 105, 105),  # 8 - dim gray
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
            (0, 0, 0),        # 0 - not used
            (255, 69, 0),     # 1 - red-orange
            (255, 140, 0),    # 2 - dark orange
            (220, 20, 60),    # 3 - crimson
            (199, 21, 133),   # 4 - medium violet red
            (139, 0, 139),    # 5 - dark magenta
            (255, 20, 147),   # 6 - deep pink
            (178, 34, 34),    # 7 - firebrick
            (139, 69, 19),    # 8 - saddle brown
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
            (0, 0, 0),        # 0 - not used
            (138, 43, 226),   # 1 - blue violet
            (255, 20, 147),   # 2 - deep pink
            (255, 69, 0),     # 3 - red-orange
            (30, 144, 255),   # 4 - dodger blue
            (255, 105, 180),  # 5 - hot pink
            (0, 206, 209),    # 6 - dark turquoise
            (186, 85, 211),   # 7 - medium orchid
            (147, 112, 219),  # 8 - medium purple
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
            (150, 150, 150),  # 0 - not used
            (100, 149, 237),  # 1 - cornflower blue
            (50, 205, 50),    # 2 - lime green
            (255, 99, 71),    # 3 - tomato
            (138, 43, 226),   # 4 - blue violet
            (255, 215, 0),    # 5 - gold
            (0, 255, 255),    # 6 - cyan
            (255, 192, 203),  # 7 - pink
            (220, 220, 220),  # 8 - gainsboro
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
            (100, 100, 100),  # 0 - not used
            (0, 200, 255),    # 1 - cyan bright
            (0, 255, 100),    # 2 - spring green
            (255, 50, 150),   # 3 - hot pink bright
            (200, 0, 255),    # 4 - purple bright
            (255, 255, 0),    # 5 - yellow
            (255, 100, 0),    # 6 - orange bright
            (100, 255, 255),  # 7 - cyan light
            (255, 150, 255),  # 8 - pink light
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
            (60, 60, 60),     # 0 - not used
            (0, 0, 180),      # 1 - blue
            (0, 120, 0),      # 2 - green
            (180, 0, 0),      # 3 - red
            (0, 0, 120),      # 4 - dark blue
            (120, 0, 0),      # 5 - dark red
            (0, 120, 120),    # 6 - teal
            (160, 160, 0),    # 7 - olive
            (140, 140, 140),  # 8 - gray
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
            (50, 50, 50),     # 0 - not used
            (100, 200, 255),  # 1 - sky blue
            (100, 255, 150),  # 2 - mint green
            (255, 150, 180),  # 3 - light pink
            (180, 100, 255),  # 4 - lavender
            (255, 200, 100),  # 5 - peach
            (100, 255, 255),  # 6 - light cyan
            (200, 150, 255),  # 7 - light purple
            (180, 180, 180),  # 8 - light gray
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
            (80, 40, 30),     # 0 - not used
            (255, 150, 50),   # 1 - orange bright
            (255, 200, 50),   # 2 - yellow-orange
            (255, 80, 80),    # 3 - red bright
            (200, 100, 50),   # 4 - burnt orange
            (150, 50, 50),    # 5 - dark red
            (255, 180, 100),  # 6 - light orange
            (220, 120, 60),   # 7 - sienna
            (180, 90, 70),    # 8 - brown-orange
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
            (100, 100, 100),  # 0 - not used
            (0, 100, 200),    # 1 - ocean blue
            (50, 150, 100),   # 2 - sea green
            (200, 80, 80),    # 3 - salmon red
            (100, 50, 150),   # 4 - purple
            (150, 80, 80),    # 5 - rosy brown
            (50, 150, 150),   # 6 - teal
            (70, 130, 180),   # 7 - steel blue
            (160, 160, 160),  # 8 - gray
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
            (100, 70, 40),    # 0 - not used
            (210, 105, 30),   # 1 - chocolate
            (255, 165, 0),    # 2 - orange
            (178, 34, 34),    # 3 - firebrick
            (160, 82, 45),    # 4 - sienna
            (139, 69, 19),    # 5 - saddle brown
            (184, 134, 11),   # 6 - dark goldenrod
            (205, 133, 63),   # 7 - peru
            (188, 143, 143),  # 8 - rosy brown
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
            (100, 80, 130),   # 0 - not used
            (138, 43, 226),   # 1 - blue violet
            (255, 105, 180),  # 2 - hot pink
            (255, 69, 0),     # 3 - red-orange
            (75, 0, 130),     # 4 - indigo
            (199, 21, 133),   # 5 - medium violet red
            (148, 0, 211),    # 6 - dark violet
            (186, 85, 211),   # 7 - medium orchid
            (216, 191, 216),  # 8 - thistle
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
            (0, 200, 0),      # 0 - not used
            (50, 255, 50),    # 1 - lime green bright
            (100, 255, 100),  # 2 - light green
            (150, 255, 150),  # 3 - pale green
            (0, 220, 0),      # 4 - green bright
            (0, 180, 0),      # 5 - green medium
            (100, 255, 150),  # 6 - mint
            (150, 255, 200),  # 7 - pale mint
            (200, 255, 200),  # 8 - very pale green
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
            (150, 60, 80),    # 0 - not used
            (255, 20, 147),   # 1 - deep pink
            (220, 20, 60),    # 2 - crimson
            (178, 34, 34),    # 3 - firebrick
            (199, 21, 133),   # 4 - medium violet red
            (219, 112, 147),  # 5 - pale violet red
            (255, 105, 180),  # 6 - hot pink
            (205, 92, 92),    # 7 - indian red
            (188, 143, 143),  # 8 - rosy brown
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
            (40, 100, 50),    # 0 - not used
            (0, 128, 0),      # 1 - green
            (34, 139, 34),    # 2 - forest green
            (0, 100, 0),      # 3 - dark green
            (50, 205, 50),    # 4 - lime green
            (60, 179, 113),   # 5 - medium sea green
            (32, 178, 170),   # 6 - light sea green
            (46, 139, 87),    # 7 - sea green
            (143, 188, 143),  # 8 - dark sea green
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
            (100, 70, 40),    # 0 - not used
            (184, 134, 11),   # 1 - dark goldenrod
            (218, 165, 32),   # 2 - goldenrod
            (205, 127, 50),   # 3 - peru
            (160, 82, 45),    # 4 - sienna
            (139, 69, 19),    # 5 - saddle brown
            (210, 105, 30),   # 6 - chocolate
            (188, 143, 143),  # 7 - rosy brown
            (222, 184, 135),  # 8 - burly wood
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
            (100, 70, 140),   # 0 - not used
            (138, 43, 226),   # 1 - blue violet
            (147, 112, 219),  # 2 - medium purple
            (153, 50, 204),   # 3 - dark orchid
            (186, 85, 211),   # 4 - medium orchid
            (216, 191, 216),  # 5 - thistle
            (221, 160, 221),  # 6 - plum
            (218, 112, 214),  # 7 - orchid
            (238, 130, 238),  # 8 - violet
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
            (100, 200, 255),  # 0 - not used
            (0, 255, 255),    # 1 - cyan
            (255, 0, 255),    # 2 - magenta
            (255, 100, 255),  # 3 - pink bright
            (100, 255, 255),  # 4 - cyan light
            (200, 100, 255),  # 5 - purple light
            (255, 255, 100),  # 6 - yellow light
            (150, 255, 200),  # 7 - mint cyan
            (255, 200, 150),  # 8 - peach light
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
            (50, 80, 30),     # 0 - not used
            (0, 128, 0),      # 1 - green
            (34, 139, 34),    # 2 - forest green
            (107, 142, 35),   # 3 - olive drab
            (85, 107, 47),    # 4 - dark olive green
            (124, 252, 0),    # 5 - lawn green
            (127, 255, 0),    # 6 - chartreuse
            (173, 255, 47),   # 7 - green yellow
            (144, 238, 144),  # 8 - light green
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
            (60, 70, 80),     # 0 - not used
            (70, 130, 180),   # 1 - steel blue
            (100, 149, 237),  # 2 - cornflower blue
            (65, 105, 225),   # 3 - royal blue
            (72, 61, 139),    # 4 - dark slate blue
            (106, 90, 205),   # 5 - slate blue
            (123, 104, 238),  # 6 - medium slate blue
            (135, 206, 250),  # 7 - light sky blue
            (176, 196, 222),  # 8 - light steel blue
        ],
    },
}
