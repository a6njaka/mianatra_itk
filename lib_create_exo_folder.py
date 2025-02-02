import json
import os

exo_dir = r"D:\Njaka_Project\Njaka_Dev_Itk\bin\Mianatra2\images"
# exo_dir = r"C:\Users\NJAKA\Desktop\itokiana_png"


exo_name = f"signe_de_comparaison"
exo_path = os.path.join(exo_dir, exo_name)
config_json_path = os.path.join(exo_path, 'config.json')

if not os.path.isdir(exo_path):
    os.mkdir(exo_path)

config = {
    "min": 20,
    "max": 25,
    "level": 3,
    "rand": True,
    "type": "entry",
    "case sensitive": True,
    "library": f"lib_compare_number",
    "comment": f"Utilisation de signe de comparaison"
}
with open(config_json_path, 'w') as outfile:
    json.dump(config, outfile, indent=3)


