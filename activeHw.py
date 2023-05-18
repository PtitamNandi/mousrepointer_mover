import time
from Quartz import (
    CGWindowListCopyWindowInfo,
    kCGWindowListOptionOnScreenOnly,
    kCGNullWindowID
)
time.sleep(5) 
def get_active_app_info():
    window_list = CGWindowListCopyWindowInfo(kCGWindowListOptionOnScreenOnly, kCGNullWindowID)
    for window in window_list:
        if window.get("kCGWindowOwnerName"):
            app_name = window["kCGWindowOwnerName"]
            window_bounds = window.get("kCGWindowBounds")
            window_x = window_bounds.get("X")
            window_y = window_bounds.get("Y")
            window_width = window_bounds.get("Width")
            window_height = window_bounds.get("Height")
            return app_name, window_x, window_y, window_width, window_height

if __name__ == "__main__":
    active_app_name, window_x, window_y, window_width, window_height = get_active_app_info()
    print("Active Application:", active_app_name)
    print("Window Coordinates: X:", window_x, "Y:", window_y)
    print("Window Size: Width:", window_width, "Height:", window_height)