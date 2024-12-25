from PIL import Image, ImageDraw, ImageFont
import shutil
import os
import re

text_list = {"A1": "Iza ny aranan'la?",
            "A2": "Iza ny anaran'i Dada?",
            "A3": "Iza ny anaran'i Neny?",
            "A4": "Firy taona ela?",
            "A5": "Aiza ela no mianatra?",
            }

exo_dir = r"C:/Users/NJAKA/Desktop/question_answer_1"
size = (600, 250)
fnt = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf', 50)

for chs in text_list:
    imgA = Image.new('RGB', size, color=(255, 255, 255))
    A = ImageDraw.Draw(imgA)
    name_imgA = exo_dir + "/{0}.png".format(chs)
    w, h = A.textsize("{0}".format(text_list[chs]), font=fnt)
    A.text(((size[0] - w) / 2, ((size[1] - h) / 2) - 0), "{0}".format(text_list[chs]), font=fnt, fill=(255, 0, 0))
    imgA.save(name_imgA)
    print(name_imgA)