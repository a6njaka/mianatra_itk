import os
import datetime
import platform

def get_folders_by_creation_date(folder_path):
    """
    Gets a list of folders in a given path, sorted by creation date.

    Args:
        folder_path: The path to the folder.

    Returns:
        A list of tuples, where each tuple contains:
        - The full path to the folder
        - The creation datetime object
        Sorted by creation date (oldest first).
        Returns an empty list if the path is not a directory or an error occurs.
    """

    if not os.path.isdir(folder_path):
        return []

    folders = []
    try:
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isdir(item_path):
                creation_time = get_creation_date(item_path)
                if creation_time: # Check if the creation time was retrieved successfully
                    folders.append((item_path, creation_time))

        folders.sort(key=lambda x: x[1])  # Sort by creation date (ascending)
        return folders

    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def get_creation_date(path):
    """
    Gets the creation date of a file or folder.  Handles Windows and other systems.
    """
    try:
        if platform.system() == 'Windows':
            return datetime.datetime.fromtimestamp(os.path.getctime(path))
        else:  # For Linux/macOS (metadata might not be reliable)
            stat = os.stat(path)
            try:
                return datetime.datetime.fromtimestamp(stat.st_birthtime)  # Try birthtime first
            except AttributeError:
                return datetime.datetime.fromtimestamp(stat.st_mtime)  # Fallback to modification time
    except Exception as e:
        print(f"Error getting creation date for {path}: {e}")
        return None  # Or handle the error as you see fit


# Example usage:
folder_path = r"D:\Njaka_Project\Njaka_Dev_Itk\bin\Mianatra2\images"  # Replace with the actual path
sorted_folders = get_folders_by_creation_date(folder_path)

if sorted_folders:
    print("Folders sorted by creation date:")
    for folder_path, creation_date in sorted_folders:
        print(f"{folder_path}: {creation_date}")
else:
    print("Could not retrieve folder list or the path is not a directory.")