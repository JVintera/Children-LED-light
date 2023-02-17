from machine import Pin
from machine import I2C
from tcs34725 import TCS34725
from time import sleep_ms
from utime import sleep
from neopixel import Neopixel


i2c_bus = I2C(1, sda=Pin(2), scl=Pin(3))
tcs = TCS34725(i2c_bus)