# SPDX-FileCopyrightText: 2023 Akruvia <akruvia@gmail.com>
#
# SPDX-License-Identifier: MIT
# Akruvia Maker Badge Encoder Example

import board
import neopixel
import keypad
import rotaryio

# ESP32-S3 TFT Feather built-in RGB LED
BUILTIN_NEOPIXEL_PIN = board.NEOPIXEL
# Starting pin of the RGB LEDs under the Kailh Choc v1 switches
UNDERSWITCH_NEOPIXEL_PIN = board.D12
# Encoder
ENCODER_A_PIN = board.A1
ENCODER_B_PIN = board.A0
ENCODER_BUTTON_PIN = board.A2

NUM_BUILTIN_PIXELS = 1
NUM_UNDERSWITCH_PIXELS = 5

builtin_pixel = neopixel.NeoPixel(
    BUILTIN_NEOPIXEL_PIN, NUM_BUILTIN_PIXELS, brightness=0.5, auto_write=False
)

underswitch_pixels = neopixel.NeoPixel(
    UNDERSWITCH_NEOPIXEL_PIN, NUM_UNDERSWITCH_PIXELS, brightness=0.5, auto_write=False
)

encoder_button = keypad.Keys((ENCODER_BUTTON_PIN,), value_when_pressed=False, pull=True)

encoder = rotaryio.IncrementalEncoder(ENCODER_A_PIN, ENCODER_B_PIN)

last_position = encoder.position

# 5 steps, 255 / 51
VALUE_MULTIPLIER = 51

# (RGB888)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CURRENT_COLOR_COMPONENT = (RED, GREEN, BLUE)

color_result = [0, 0, 0]
color_component_index = 0

while True:
    current_position = encoder.position
    position_change = current_position - last_position
    event = encoder_button.events.get()
    if event:
        key_number = event.key_number
        if event.pressed:
            if color_component_index == 2:
                color_component_index = 0
            else:
                color_component_index = color_component_index + 1

    if position_change > 0:
        color_result[color_component_index] = color_result[color_component_index] + (
            position_change * VALUE_MULTIPLIER
        )
        if color_result[color_component_index] > 255:
            color_result[color_component_index] = 255
    elif position_change < 0:
        color_result[color_component_index] = color_result[color_component_index] + (
            position_change * VALUE_MULTIPLIER
        )
        if color_result[color_component_index] < 0:
            color_result[color_component_index] = 0

    last_position = current_position

    # Current color component that is being adjusted
    builtin_pixel.fill(CURRENT_COLOR_COMPONENT[color_component_index])
    # Color result
    for i in range(2):
        underswitch_pixels[i] = tuple(color_result)
    # Red component value
    underswitch_pixels[2] = (color_result[0], 0, 0)
    # Green component value
    underswitch_pixels[3] = (0, color_result[1], 0)
    # Blue component value
    underswitch_pixels[4] = (0, 0, color_result[2])
    builtin_pixel.show()
    underswitch_pixels.show()
