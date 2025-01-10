import os
import json


def convert_txt_to_json(base_folder):
    # Walk through all subfolders
    for root, dirs, files in os.walk(base_folder):
        # Check if "stage_config.txt" exists in the current folder
        if "stage_config.txt" in files:
            txt_file_path = os.path.join(root, "stage_config.txt")
            json_file_path = os.path.join(root, "config.json")

            # Read the content of "stage_config.txt"
            config = {}
            with open(txt_file_path, 'r') as txt_file:
                for line in txt_file:
                    # Skip empty or improperly formatted lines
                    if " = " not in line:
                        continue
                    key, value = line.strip().split(' = ', 1)
                    config[key] = value

            # Map the values to the JSON structure
            json_data = {
                "min": 5,
                "max": int(config.get("MaxStage", 10)),
                "level": 0,
                "rand": config.get("Rand", "No").lower() == "yes",
                "type": "entry",
                "case sensitive": config.get("CaseSensitive", "False").lower() == "true",
                "comment": config.get("Comment", "")
            }

            # Write to "config.json"
            with open(json_file_path, 'w') as json_file:
                json.dump(json_data, json_file, indent=4)
            print(f"Converted: {txt_file_path} -> {json_file_path}")


# Replace 'base_folder' with the path to your base folder
base_folder = r"D:\Njaka_Project\Njaka_Dev_Itk\bin\Mianatra2\images"
convert_txt_to_json(base_folder)
