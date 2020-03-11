from neopixel import Neopixel
from machine import Pin
from random import choice
from time import sleep

np = Neopixel(Pin(4), 8)


def val_gen():
  yield choice(range(255))


def color_gen():
  yield tuple(next(val_gen()) for i in range(3))


while True:

  np[choice(range(8))] = next(color_gen())
  sleep(0.5)
