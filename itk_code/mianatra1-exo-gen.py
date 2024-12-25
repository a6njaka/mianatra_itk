from PIL import Image, ImageDraw, ImageFont
import os

comulnA = ["A1", "A2²", "A3", "A4", "A5"]
comulnB = ["B1", "B2", "B3", "B4", "B5"]

fnt1 = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 40)
fnt2 = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 40)

exo_dir = r"C:/Users/NJAKA/Desktop/test/"

if not os.path.exists(exo_dir):
    os.makedirs(exo_dir)

image_width = 160
image_height = 80

for i in range(1, 6):
    imgA = Image.new('RGB', (image_width, image_height), color=(255, 255, 255))
    imgB = Image.new('RGB', (image_width, image_height), color=(255, 255, 255))

    A = ImageDraw.Draw(imgA)
    B = ImageDraw.Draw(imgB)

    name_imgA = exo_dir + "A{0}.png".format(i)
    name_imgB = exo_dir + "B{0}.png".format(i)

    # a + b = c
    w_a, h_a = A.textsize("{0}".format(comulnA[i - 1]), font=fnt1)
    w_b, h_b = A.textsize("{0}".format(comulnB[i - 1]), font=fnt1)

    wd = 0

    w_sign, h_sign = A.textsize("+", font=fnt1)

    x_center = image_width / 2
    y_center = image_height / 2

    A.text((x_center - (w_a / 2), y_center - (h_a / 2)), "{0}".format(comulnA[i - 1]), font=fnt2, fill=(0, 200, 0))
    B.text((x_center - (w_b / 2), y_center - (h_b / 2)), "{0}".format(comulnB[i - 1]), font=fnt2, fill=(0, 200, 0))

    # print("{0}".format(exo[i - 1][0] + exo[i - 1][1]))

    imgA.save(name_imgA)
    imgB.save(name_imgB)

    print(name_imgA)
    print(name_imgB)
