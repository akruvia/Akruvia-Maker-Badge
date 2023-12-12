# SPDX-FileCopyrightText: 2023 Akruvia <akruvia@gmail.com>
#
# SPDX-License-Identifier: MIT
# Akruvia Maker Badge Blink Example

import board

# ESP32-S3 TFT Feather display
display = board.DISPLAY
# Do not show CircuitPython REPL on LCD
display.root_group.hidden = True
# Turn off LCD backlight
display.brightness = 0
