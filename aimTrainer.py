import pyautogui
import time
import keyboard

# Ask the user to hover over the top-left corner of the game area and press 's'
print("Hover over the top-left corner of the game area and press 's'.")
keyboard.wait('s')
top_left_x, top_left_y = pyautogui.position()

# Ask the user to hover over the bottom-right corner of the game area and press 's'
print("Now hover over the bottom-right corner of the game area and press 's'.")
keyboard.wait('s')
bottom_right_x, bottom_right_y = pyautogui.position()

# Calculate the width and height of the game area
width = bottom_right_x - top_left_x
height = bottom_right_y - top_left_y

# Generate a list of all (x, y) coordinates in the search space
coordinates = [(x, y) for x in range(0, width, 5) for y in range(0, height, 5)]

# The target color to look for (white in this case)
target_color = (149, 195, 232)

print("Hover over a target and press 's' to start the clicking.")
keyboard.wait('s')

pyautogui.click()

click_count = 0
while click_count < 35:
      # Take a new screenshot of the specified region to get the latest target positions
      screenshot = pyautogui.screenshot(region=(top_left_x, top_left_y, width, height))

      for x, y in coordinates:
            pixel_color = screenshot.getpixel((x, y))

            if pixel_color == target_color:
                  pyautogui.click(top_left_x + x, top_left_y + y)
                  click_count += 1
                  # A delay here might be necessary to allow the target to move and the game to update
                  # especially if the game has animations or a delay before a new target appears.
                  time.sleep(0.01)
                  break  # Break after clicking to take a new screenshot
      

print("All targets clicked!")