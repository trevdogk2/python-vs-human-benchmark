import pyautogui

while True:
    x, y = pyautogui.position()
    rgb_red = pyautogui.pixel(x, y)[0]

    if rgb_red == 75 or rgb_red == 43:
        pyautogui.click()