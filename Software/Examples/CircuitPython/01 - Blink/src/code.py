# SPDX-FileCopyrightText: 2023 Akruvia <akruvia@gmail.com>
#
# SPDX-License-Identifier: MIT
# Akruvia Maker Badge Blink Example

import board
import neopixel
import digitalio
import time

# ESP32-S3 TFT Feather built-in RGB LED
BUILTIN_NEOPIXEL_PIN = board.NEOPIXEL
# ESP32-S3 TFT Feather built-in Red LED
RED_LED_PIN = board.LED
# RGB LEDs under the Kailh Choc v1 switches
UNDERSWITCH_NEOPIXEL_PIN = board.D12

NUM_BUILTIN_PIXELS = 1
NUM_UNDERSWITCH_PIXELS = 5

builtin_pixel = neopixel.NeoPixel(
    BUILTIN_NEOPIXEL_PIN, NUM_BUILTIN_PIXELS, brightness=0.1, auto_write=False
)

underswitch_pixels = neopixel.NeoPixel(
    UNDERSWITCH_NEOPIXEL_PIN, NUM_UNDERSWITCH_PIXELS, brightness=0.1, auto_write=False
)

red_led = digitalio.DigitalInOut(RED_LED_PIN)
red_led.direction = digitalio.Direction.OUTPUT

# (RGB888)
BLANK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
PURPLE = (255, 0, 255)

COLORS = (
    RED,
    BLANK,
    GREEN,
    BLANK,
    BLUE,
    BLANK,
    YELLOW,
    BLANK,
    CYAN,
    BLANK,
    PURPLE,
    BLANK,
)

while True:
    for i, color in enumerate(COLORS):
        builtin_pixel.fill(color)
        underswitch_pixels.fill(color)
        builtin_pixel.show()
        underswitch_pixels.show()
        # Check if i is even or odd
        if i & 1:
            red_led.value = False
        else:
            red_led.value = True
        time.sleep(0.25)
