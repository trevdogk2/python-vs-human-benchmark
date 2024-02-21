import pyautogui
import time

while True:
    time.sleep(1)
    x, y = pyautogui.position()  # Get the current mouse position.
    px = pyautogui.pixel(x, y)   # Get the pixel color at the mouse position.
    print("px", px)