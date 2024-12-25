from PIL import Image, ImageDraw, ImageFont
import shutil
import os
import re

# -------------------Setting-------------------------
exo_dir = r"C:/Users/NJAKA/Desktop/shape_2/"
answer = {"C1": "60",
          "C2": "70",
          "C3": "80",
          "C4": "90",
          "C5": "100",
          }
res = {"A1": "C1",
       "A2": "C2",
       "A3": "C3",
       "A4": "C4",
       "A5": "C5",
       "A6": "C1",
       }
rand = True
comment = True
goal = "Mianatra"
# ---------------------------------------------------
generate_answer = False
# ---------------------------------------------------

# ---------------Cleaning---------------
files = []
# r=root, d=directories, f = files
print("-" * 50)
for r, d, f in os.walk(exo_dir):
    for file in f:
        if '.png' in file:
            m = re.match("^B", file)
            if m is not None:
                files.append(file)
                try:
                    os.remove(os.path.join(r, file))
                except FileNotFoundError:
                    print(f"The file \"{file}\" cannot be found")
# -----------End-Cleaning---------------

fnt1 = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf', 50)
fnt2 = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf', 50)

if not os.path.exists(exo_dir):
    os.makedirs(exo_dir)
choices = exo_dir + "choices"
if not os.path.exists(choices):
    os.makedirs(choices)

if generate_answer:
    for chs in answer:
        imgC = Image.new('RGB', (120, 80), color=(255, 255, 255))
        C = ImageDraw.Draw(imgC)
        name_imgC = choices + "/{0}.png".format(chs)
        w, h = C.textsize("{0}".format(answer[chs]), font=fnt2)
        C.text(((120 - w) / 2, ((80 - h) / 2) - 0), "{0}".format(answer[chs]), font=fnt2, fill=(30, 2, 193))
        imgC.save(name_imgC)
        print(name_imgC)

for exo in res:
    source = exo_dir + "{}.png".format(exo)
    cr_ans = f"{choices}/{res[exo]}.png"
    destination = exo_dir + "{}-{}.png".format(exo.replace("A", "B"), res[exo])
    if os.path.isfile(source) and os.path.isfile(cr_ans):
        print(f"{source}  <-->  {destination}")
        shutil.copyfile(source, destination)

rand_file = choices + '/rand.txt'
if rand:
    try:
        f = open(rand_file, 'w')
        f.write('rand the choices')
        f.close()
    except PermissionError:
        print("Error while creating file", rand_file)
else:
    try:
        if os.path.exists(rand_file):
            os.remove(rand_file)
    except PermissionError:
        print("Error while deleting file ", rand_file)

if comment:
    try:
        f = open(exo_dir + '/comment.txt', 'w')
        f.write(goal)
        text = ""
        if generate_answer:
            for t in answer:
                text += f"{answer[t]},"
            f.write(f"\n{text.strip(',')}")
        f.close()
    except PermissionError:
        print("Error while creating file", rand_file)
else:
    try:
        os.remove(rand_file)
    except PermissionError:
        print("Error while deleting file ", rand_file)
