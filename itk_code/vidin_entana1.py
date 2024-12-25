from PIL import Image, ImageDraw, ImageFont
import os
import re
import stage_config
from shutil import copyfile

exo = {}
n = 0
for i in range(10, 30):
    n += 1
    exo[f"E{i}"] = [i, i % 2]

answer = ["100","200", "300", "500", "600"]

# Exo format "ANY": ["TEXT", #] | TEXT can be a string or image.png # is index in the answer
exo = [
    ["entana1.png", "Hoatrinona ny mofogasy.mp3", "100"],
    ["entana1.png", "Hoatrinona ny ramanonaka.mp3", "100"],
    ["entana1.png", "Hoatrinona ny madeleine.mp3", "500"],
    ["entana1.png", "Hoatrinona ny menakely.mp3", "300"],
    ["entana1.png", "Hoatrinona ny mofobaolina.mp3", "300"],
    ["entana1.png", "Hoatrinona ny sambos.mp3", "300"],
    ["entana1.png", "Hoatrinona ny makasaoka.mp3", "300"],
    ["entana1.png", "Hoatrinona ny caca pigeon.mp3", "500"],
    ["entana1.png", "Hoatrinona ny donut.mp3", "500"],
    ["entana1.png", "Hoatrinona ny mofo dipaina.mp3", "600"],
    ["entana1.png", "Hoatrinona ny frais mankany ravitoto.mp3", "500"],
    ["entana1.png", "Hoatrinona ny frais mankany analakely.mp3", "600"],
]

print(exo)

fnt1 = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf', 80)
fnt2 = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf', 80)

exo_dir = "C:/Users/NJAKA/Desktop/vidin_entana1/"
mp3_source = "vidin_entana1_data/"
images_source = "vidin_entana1_data/"

if not os.path.exists(exo_dir):
    os.makedirs(exo_dir)
choices = exo_dir + "choices"
if not os.path.exists(choices):
    os.makedirs(choices)

stage_config.create_dir(exo_dir)
stage_config.clean(exo_dir)

for i in range(len(exo)):
    data = exo[i]
    name_imgA = exo_dir + f"A{i + 1}.png"
    name_mp3A = exo_dir + f"A{i + 1}.mp3"
    try:
        name_imgB = exo_dir + f"B{i + 1}-C{answer.index(data[2]) + 1}.png"
    except:
        print(f"---ERROR_01-->'{data}'")

    # Copy mp3 if exist
    print(f"'{mp3_source}{data[1]}'->'{name_mp3A}'")
    if os.path.exists(f"{mp3_source}{data[1]}"):
        copyfile(f"{mp3_source}{data[1]}", name_mp3A)

    # Copy PNG if exist
    if os.path.exists(f"{images_source}{data[0]}"):
        copyfile(f"{images_source}{data[0]}", name_imgA)
        copyfile(f"{images_source}{data[0]}", name_imgB)

    else:
        w_exo = 600
        h_exo = 250
        imgA = Image.new('RGB', (w_exo, h_exo), color=(255, 255, 255))
        imgB = Image.new('RGB', (w_exo, h_exo), color=(255, 255, 255))

        A = ImageDraw.Draw(imgA)
        B = ImageDraw.Draw(imgB)
        sign = ""

        w, h = A.textsize("{0}".format(exo[data][0]), font=fnt1)

        A.text(((w_exo - w) / 2, (h_exo - h) / 2), "{0}".format(exo[data][0]), font=fnt1, fill=(1, 4, 254))
        B.text(((w_exo - w) / 2, (h_exo - h) / 2), "{0}".format(exo[data][0]), font=fnt1, fill=(1, 4, 254))

        imgA.save(name_imgA)
        imgB.save(name_imgB)

        print(name_imgA)
        print(name_imgB)

j = 1
for text in answer:
    fnt3 = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf', 30)
    imgC = Image.new('RGB', (120, 80), color=(255, 255, 255))
    C = ImageDraw.Draw(imgC)
    w, h = C.textsize(f"{text}", font=fnt3)
    C.text(((120 - w) / 2, (80 - h) / 2), text, font=fnt3, fill=(250, 0, 0))
    name_imgC = choices + "/C{0}.png".format(j)
    imgC.save(name_imgC)
    if os.path.exists(f"{mp3_source}{text}.mp3"):
        copyfile(f"{mp3_source}{text}.mp3", f"{choices}/C{j}.mp3")
    j += 1

stage_config.config(exo_dir, 10, "pair et impaire", "Yes", "True")
