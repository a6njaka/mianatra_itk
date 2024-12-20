from PIL import Image, ImageDraw, ImageFont
import shutil
import os
import re
from shutil import copyfile
from shutil import copyfile
from sys import exit
import sys
import random
import math


class Exercise:
    def __init__(self, exo_dir, mp3_source, images_source, exo_setting=[10, "", "Yes", "True"], font_exo=None, font_question=None, red_pos=-1):
        self.w = 600
        self.h = 250
        self.exo_dir = exo_dir
        self.mp3_source = mp3_source
        self.images_source = images_source
        self.red = red_pos
        self.exo_number = 0
        if font_exo is None:
            self.font_exo = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf', 15)
        else:
            self.font_exo = font_exo
        if font_question is None:
            self.font_question = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf', 20)
        else:
            self.font_question = font_question
        print("*" * 100)
        self.generate_images_list()
        print(f"Number of exo = {self.exo_number }")
        self.imgA = None
        self.A = None
        self.imgB = None
        self.B = None
        print("*" * 100)

    def generate_images_list(self):
        print("-->generate_images_list++")
        i = 1
        vola_list = [100, 200, 500, 1000, 2000, 5000]
        # vola_list = [100, 200]
        for vola1 in vola_list:
            for vola2 in vola_list:
                for vola3 in vola_list:
                    self.imgA = Image.new('RGB', (self.w, self.h), color=(255, 255, 255))
                    self.imgB = Image.new('RGB', (self.w, self.h), color=(255, 255, 255))
                    name_imgA = exo_dir + "A{0}.png".format(i)
                    name_imgB = exo_dir + "B{0}-{1}.png".format(i, vola1 + vola2 + vola3)

                    self.A = ImageDraw.Draw(self.imgA)
                    self.B = ImageDraw.Draw(self.imgB)
                    sary_vola1 = Image.open(rf"vola\{vola1}.jpg")
                    sary_vola2 = Image.open(rf"vola\{vola2}.jpg")
                    sary_vola3 = Image.open(rf"vola\{vola3}.jpg")
                    width1, height1 = sary_vola1.size
                    width2, height2 = sary_vola2.size
                    width3, height3 = sary_vola3.size
                    div = 2
                    img_vola1 = sary_vola1.resize((int(width1 / div), int(height1 / div)))
                    img_vola2 = sary_vola2.resize((int(width2 / div), int(height2 / div)))
                    img_vola3 = sary_vola3.resize((int(width3 / div), int(height3 / div)))

                    self.A.text((10, 2), "Hoatrinona ireo vola ireo? (Tsy asina Ar/Ariary)", font=self.font_exo, fill=(0, 0, 0))
                    self.imgA.paste(img_vola1, (50, 30))
                    self.imgA.paste(img_vola2, (150, 50))
                    self.imgA.paste(img_vola3, (250, 70))

                    self.B.text((10, 2), "Hoatrinona ireo vola ireo? (Tsy asina Ar/Ariary)", font=self.font_exo, fill=(0, 0, 0))
                    self.imgB.paste(img_vola1, (50, 30))
                    self.imgB.paste(img_vola2, (150, 50))
                    self.imgB.paste(img_vola3, (250, 70))
                    self.imgA.save(name_imgA)
                    self.imgB.save(name_imgB)

                i += 1
        self.exo_number = i


exo_dir = fr"C:/Users/NJAKA/Desktop/Addition_vola_2/"
mp3_source = "D:/Itokiana-python/mp3/"
images_source = "D:/Itokiana-python/mp3/"
q = ""
exo_setting = [10, f"Addition_vola_02", "Yes", "True"]

p1 = Exercise(exo_dir=exo_dir, mp3_source=mp3_source, images_source=images_source, exo_setting=exo_setting, red_pos=4)
