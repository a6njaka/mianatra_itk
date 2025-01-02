import json

data = {
    "min": 1,
    "max": 5,
    "level": 0,
    "rand": False,
    "type": "entry",
    "case sensitive": False,
    "comment": "",
}

with open(r"C:\Users\NJAKA\Desktop\exo_itk\config.json", 'w') as outfile:
    json.dump(data, outfile, indent=3)
