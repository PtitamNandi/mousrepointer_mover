import time
from Quartz import (
    CGWindowListCopyWindowInfo,
    kCGWindowListOptionOnScreenOnly,
    kCGNullWindowID
)
import pyautogui

def get_active_app_window(app_name):
    window_list = CGWindowListCopyWindowInfo(kCGWindowListOptionOnScreenOnly, kCGNullWindowID)
    for window in window_list:
        if window.get("kCGWindowOwnerName") == app_name and window.get("kCGWindowIsOnscreen"):
            # print(window)
            return window

    return None

if __name__ == "__main__":
    app_name = "Time Champ"  # Replace with the desired application name
    x = 500  # Replace with your desired x-coordinate
    y = 300  # Replace with your desired y-coordinate

    while True:
        active_app_window = get_active_app_window(app_name)

        if active_app_window is not None:
            window_bounds = active_app_window.get("kCGWindowBounds")
            window_x = window_bounds.get("X")
            window_y = window_bounds.get("Y")

            target_x = window_x + x
            target_y = window_y + y

            pyautogui.click(target_x, target_y)

        # Adjust the delay as needed between detections
        time.sleep(1)
# import pyautogui

# # Specify the target coordinates
# x = 500  # Replace with your desired x-coordinate
# y = 300  # Replace with your desired y-coordinate

# # Move the mouse pointer to the specified coordinates
# pyautogui.moveTo(x, y)
# from screeninfo import get_monitors

# # Get the primary monitor
# monitor = get_monitors()[0]

# # Retrieve the screen width and height
# screen_width = monitor.width
# screen_height = monitor.height

# # Print the screen size
# print(f"Screen size: {screen_width}x{screen_height}")