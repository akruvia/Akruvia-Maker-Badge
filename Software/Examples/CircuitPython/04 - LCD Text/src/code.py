# SPDX-FileCopyrightText: 2023 Akruvia <akruvia@gmail.com>
#
# SPDX-License-Identifier: MIT
# Akruvia Maker Badge LCD Text Example

import board
import displayio
import terminalio
from adafruit_display_text import label

# ESP32-S3 TFT Feather display
display = board.DISPLAY

# Background
NUM_PALETTE_COLOR = 1
background_bitmap = displayio.Bitmap(display.width, display.height, NUM_PALETTE_COLOR)
palette = displayio.Palette(NUM_PALETTE_COLOR)
# White (RGB888)
palette[0] = 0xFFFFFF
background = displayio.TileGrid(background_bitmap, pixel_shader=palette)

# Text
TEXT = "Akruvia\nMaker Badge"
FONT = terminalio.FONT
# Black (RGB888)
COLOR = 0x000000

# Label
akruvia_maker_badge_label = label.Label(FONT, text=TEXT, color=COLOR, scale=3)
# Center position
akruvia_maker_badge_label.anchor_point = (0.5, 0.5)
akruvia_maker_badge_label.anchored_position = (display.width / 2, display.height / 2)

# Group things together for root_group
group = displayio.Group()

# Mind the order of appending, this is layered
group.append(background)
group.append(akruvia_maker_badge_label)

# Show
display.root_group = group

# Loop to not exit the program
while True:
    pass
