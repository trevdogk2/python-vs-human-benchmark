import pyautogui
import time
import keyboard  # Import the keyboard library

# Wait for the user to press 's' before starting the loop
print("Press 's' to start the script...")
keyboard.wait('s')

epoch = 0

while epoch < 5:
    x, y = pyautogui.position()  # Get the current mouse position.
    red = pyautogui.pixel(x, y)[0]  # Get the red pixel value at the mouse position.

    match red:
        case 43:    # BLUE
              print("Starting Round...")
              time.sleep(1)
              pyautogui.click()
        # case 206:   # RED
        #       continue
        case 75:    # GREEN
              pyautogui.click()
              print("GREEN!")
              epoch+=1


print("Well Done!")