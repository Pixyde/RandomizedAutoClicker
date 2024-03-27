import random

from pynput import keyboard, mouse
import time

on = False
def on_press(key):
    if key == keyboard.Key.f6:
        global on
        on = not on

listener = keyboard.Listener(on_press=on_press)
listener.start()

mouse_controller = mouse.Controller()

while True:
    if on:
        mouse_controller.click(mouse.Button.left, 1)
        time.sleep(random.randint(700, 1000) / 10000)
    time.sleep(0.0001)