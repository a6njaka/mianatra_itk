import json
import os

exo_dir = r"D:\Njaka_Project\Njaka_Dev_Itk\bin\Mianatra2\images"
# exo_dir = r"C:\Users\NJAKA\Desktop\itokiana_png"


def crete_exo(i):
    exo_name = f"multiplication_par_{i}_ver"
    exo_path = os.path.join(exo_dir, exo_name)
    config_json_path = os.path.join(exo_path, 'config.json')

    if not os.path.isdir(exo_path):
        os.mkdir(exo_path)

    config = {
        "min": 10,
        "max": 15,
        "level": 1,
        "rand": True,
        "type": "entry",
        "case sensitive": True,
        "library": f"lib_multiplication_par_{i}_ver",
        "comment": f"Multiplication par {i}"
    }
    with open(config_json_path, 'w') as outfile:
        json.dump(config, outfile, indent=3)


for i in range(2, 10):
    crete_exo(i)
