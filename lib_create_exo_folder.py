import json
import os

exo_dir = r"D:\Njaka_Project\Njaka_Dev_Itk\bin\Mianatra2\images"
# exo_dir = r"C:\Users\NJAKA\Desktop\itokiana_png"


exo_name = f"montre_a_aiguilles"
exo_path = os.path.join(exo_dir, exo_name)
config_json_path = os.path.join(exo_path, 'config.json')

if not os.path.isdir(exo_path):
    os.mkdir(exo_path)

config = {
    "min": 10,
    "max": 15,
    "level": 3,
    "rand": True,
    "type": "entry",
    "case sensitive": True,
    "library": f"lib_analog_clock",
    "comment": f"Exercice montre à aiguilles"
}
with open(config_json_path, 'w') as outfile:
    json.dump(config, outfile, indent=3)


