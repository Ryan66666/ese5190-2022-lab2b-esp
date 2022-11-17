# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries

# SPDX-License-Identifier: MIT

"""CircuitPython Essentials HID Keyboard example"""
import time
import board
import digitalio
import usb_hid
import busio
import neopixel
import adafruit_apds9960.apds9960
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_apds9960.apds9960 import APDS9960

i2c = board.STEMMA_I2C()
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
apds = APDS9960(i2c)
apds.enable_proximity = True
apds.enable_gesture = False
apds.enable_color = True

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
sensor.color_integration_time = 10
while True:
    r, g, b, c = sensor.color_data
    #print('Red: {0}, Green: {1}, Blue: {2}, Clear: {3}'.format(r, g, b, c))
    pixels.fill((c, c, 0))
