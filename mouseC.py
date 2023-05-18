import math
import time
import pyautogui

# Define the center of the circle and its radius
center_x = 500  # Replace with the desired x-coordinate of the circle center
center_y = 300  # Replace with the desired y-coordinate of the circle center
radius = 100  # Replace with the desired radius of the circle

# Calculate the angle increment for each step
num_steps = 360  # Number of steps to complete the circle
angle_increment = 2 * math.pi / num_steps

# Define the target coordinate for the click action
target_x = 600  # Replace with the desired x-coordinate of the target point
target_y = 300  # Replace with the desired y-coordinate of the target point

# Move the mouse pointer in a circular path
for i in range(num_steps):
    # Calculate the angle for the current step
    angle = i * angle_increment

    # Calculate the current position on the circle
    x = center_x + int(radius * math.cos(angle))
    y = center_y + int(radius * math.sin(angle))

    # Move the mouse pointer to the current position
    pyautogui.moveTo(x, y)
    time.sleep(0.01)  # Adjust the delay between steps if needed

# Perform a click action on the target coordinate
pyautogui.click(target_x, target_y)
