from PIL import Image, ImageDraw, ImageFont
import shutil
import os
import re
from shutil import copyfile
from shutil import copyfile
from sys import exit
import sys
import stage_config
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
            self.font_exo = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf', 50)
        else:
            self.font_exo = font_exo
        if font_question is None:
            self.font_question = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf', 20)
        else:
            self.font_question = font_question
        stage_config.create_dir(self.exo_dir)
        stage_config.clean(self.exo_dir)
        print("*" * 100)
        # stage_config.generate_pdf2(exo_dir)
        self.generate_images_list()
        stage_config.config(exo_dir, exo_setting[0], exo_setting[1], exo_setting[2], exo_setting[3])
        print(f"Number of exo = {self.exo_number }")
        self.imgA = None
        self.A = None
        self.imgB = None
        self.B = None
        print("*" * 100)

    def generate_images_list(self):
        print("-->generate_images_list++")
        i = 1
        for vola1 in [100, 200, 500, 1000, 2000, 5000]:
            for vola2 in [100, 200, 500, 1000, 2000, 5000]:
                self.imgA = Image.new('RGB', (self.w, self.h), color=(255, 255, 255))
                self.imgB = Image.new('RGB', (self.w, self.h), color=(255, 255, 255))
                name_imgA = exo_dir + "A{0}.png".format(i)
                name_imgB = exo_dir + "B{0}-{1}.png".format(i, vola1 + vola2)

                self.A = ImageDraw.Draw(self.imgA)
                self.B = ImageDraw.Draw(self.imgB)
                sary_vola1 = Image.open(rf"vola\{vola1}.jpg")
                sary_vola2 = Image.open(rf"vola\{vola2}.jpg")
                width1, height1 = sary_vola1.size
                width2, height2 = sary_vola2.size
                div = 2.5
                img_vola1 = sary_vola1.resize((int(width1 / div), int(height1 / div)))
                img_vola2 = sary_vola2.resize((int(width1 / div), int(height1 / div)))
                self.imgA.paste(img_vola1, (23, 60))
                self.imgA.paste(img_vola2, (340, 60))
                self.A.text((285, 100), "+", font=self.font_exo, fill=(0, 0, 0))
                self.imgB.paste(img_vola1, (23, 60))
                self.imgB.paste(img_vola2, (340, 60))
                self.B.text((285, 100), "+", font=self.font_exo, fill=(0, 0, 0))
                self.imgA.save(name_imgA)
                self.imgB.save(name_imgB)

                i += 1
        self.exo_number = i



exo_dir = fr"C:/Users/NJAKA/Desktop/Addition_vola_1/"
mp3_source = "D:/Itokiana-python/mp3/"
images_source = "D:/Itokiana-python/mp3/"
q = ""
exo_setting = [10, f"Addition_vola_01", "Yes", "True"]

p1 = Exercise(exo_dir=exo_dir, mp3_source=mp3_source, images_source=images_source, exo_setting=exo_setting, red_pos=4)
