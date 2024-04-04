import pyautogui
import time
import keyboard
import numpy as np
from mss import mss

# Disable PyAutoGUI's failsafe
pyautogui.FAILSAFE = False
pyautogui.MINIMUM_DURATION = 0.0
pyautogui.MINIMUM_SLEEP = 0.0

# Use a window width of 1009px
# Hover over the top-left corner of the game area and press 's'
print("Hover over the top-left corner of the game area and press 's'.")
keyboard.wait('s')
top_left_x, top_left_y = pyautogui.position()

# Hover over the bottom-right corner of the game area and press 's'
print("Now hover over the bottom-right corner of the game area and press 's'.")
keyboard.wait('s')
bottom_right_x, bottom_right_y = pyautogui.position()

# Calculate the width and height of the game area
width = bottom_right_x - top_left_x
height = bottom_right_y - top_left_y

# Create an MSS object for taking screenshots
sct = mss()

# Define the monitor region to capture
monitor = {"top": top_left_y, "left": top_left_x, "width": width, "height": height}

# The target color to look for (white in this case)
target_color = (149, 195, 232)

print("Hover over a target and press 's' to start the clicking.")
keyboard.wait('s')
pyautogui.click()
click_count = 0
step = 69


# Take a screenshot of the specified region
screenshot = sct.grab(monitor)

# Convert the screenshot to a numpy array
img = np.array(screenshot)

print("Screenshot shape:", img.shape)
print("Screenshot data type:", img.dtype)
print("Screenshot:\n", img)

# Select the RGB channels of the image
img_rgb = img[:, :, :3]

print("RGB channels shape:", img_rgb.shape)
print("RGB channels data type:", img_rgb.dtype)
print("RGB channels:\n", img_rgb)

# Compare each pixel's RGB values with the target color
color_match = img_rgb == target_color

print("Color match shape:", color_match.shape)
print("Color match data type:", color_match.dtype)
print("Color match:\n", color_match)

# Check if all three color channels match the target color for each pixel
all_match = np.all(color_match, axis=-1)

print("All match shape:", all_match.shape)
print("All match data type:", all_match.dtype)
print("All match:\n", all_match)

# Find the indices of the matching pixels
target_indices = np.where(all_match)

print("Target indices:", target_indices)
# while click_count < 35:
#       # Take a screenshot of the specified region
#       screenshot = sct.grab(monitor)
      
#       # Convert the screenshot to a numpy array
#       img = np.array(screenshot)
#       print('===')
#       print('===')
#       print('===')
#       print('===')
#       print('===')
#       print('===')
#       print(img)
      
#       # Find the first occurrence of the target color
#       target_index = np.where(np.all(img[:, :, :3] == target_color, axis=-1))
      
#       if len(target_index[0]) > 0:
#             # Get the first target pixel location
#             target_y, target_x = target_index[0][0], target_index[1][0]
            
#             # Click on the target pixel
#             pyautogui.click(top_left_x + target_x, top_left_y + target_y)
#             click_count += 1
#             time.sleep(0.005)  # Adjust the sleep duration as needed
        
#       if click_count >= 35:
#         break

print("All targets clicked!")