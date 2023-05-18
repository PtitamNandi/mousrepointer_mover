# import time
# import objc
# from AppKit import NSWorkspace

# time.sleep(5) 
# def get_active_app_name():
#     print("hi")
#     shared_workspace = NSWorkspace.sharedWorkspace()
#     active_app = shared_workspace.activeApplication()
#     app_name = active_app['NSApplicationName']
#     return app_name

# if __name__ == "__main__":
#     active_app_name = get_active_app_name()
#     print("Active Application:", active_app_name)


import objc
from AppKit import NSWorkspace
import pyautogui
import time

def get_active_app_name():
    shared_workspace = NSWorkspace.sharedWorkspace()
    active_app = shared_workspace.activeApplication()
    app_name = active_app['NSApplicationName']
    return app_name

if __name__ == "__main__":
    target_app_name = "Time Champ"  # Replace with the desired application name
    target_x = 500  # Replace with the desired x-coordinate
    target_y = 300  # Replace with the desired y-coordinate

    while True:
        active_app_name = get_active_app_name()
        print("Active Application:", active_app_name)

        if active_app_name == target_app_name:
            pyautogui.click(target_x, target_y)

        time.sleep(2)