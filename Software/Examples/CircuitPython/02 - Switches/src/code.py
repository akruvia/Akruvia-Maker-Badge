# SPDX-FileCopyrightText: 2023 Akruvia <akruvia@gmail.com>
#
# SPDX-License-Identifier: MIT
# Akruvia Maker Badge Switches Example

import board
import neopixel
import keypad

# ESP32-S3 TFT Feather built-in RGB LED
BUILTIN_NEOPIXEL_PIN = board.NEOPIXEL
# RGB LEDs under the Kailh Choc v1 switches
UNDERSWITCH_NEOPIXEL_PIN = board.D12
# Encoder switch + mechanical switches
KEY_PINS = (board.A2, board.D6, board.D5, board.D11, board.D10, board.D9)

NUM_BUILTIN_PIXELS = 1
NUM_UNDERSWITCH_PIXELS = 5

builtin_pixel = neopixel.NeoPixel(
    BUILTIN_NEOPIXEL_PIN, NUM_BUILTIN_PIXELS, brightness=0.1, auto_write=False
)

underswitch_pixels = neopixel.NeoPixel(
    UNDERSWITCH_NEOPIXEL_PIN, NUM_UNDERSWITCH_PIXELS, brightness=0.1, auto_write=False
)

keys = keypad.Keys(KEY_PINS, value_when_pressed=False, pull=True)

# (RGB888)
BLANK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
PURPLE = (255, 0, 255)

COLORS = (YELLOW, CYAN, PURPLE, RED, GREEN, BLUE)

while True:
    event = keys.events.get()
    if event:
        key_number = event.key_number
        if event.pressed:
            if key_number == 0:
                builtin_pixel[0] = COLORS[0]
            else:
                underswitch_pixels[key_number - 1] = COLORS[key_number]
        if event.released:
            if key_number == 0:
                builtin_pixel[0] = BLANK
            else:
                underswitch_pixels[key_number - 1] = BLANK
        underswitch_pixels.show()
        builtin_pixel.show()
