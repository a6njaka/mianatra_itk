from PIL import Image, ImageDraw, ImageFont
import os

exo = [
    [7, 2],
    [5, 3],
    [4, 8],
    [1, 6],
    [3, 3],
    [9, 9]
]

exo_num = [1, 2, 3, 4, 5, 6]
answer = ["<", ">", "="]

fnt1 = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 70)
fnt2 = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 80)

exo_dir = "C:/Users/NJAKA/Desktop/comparison_sign/"

if not os.path.exists(exo_dir):
    os.makedirs(exo_dir)
choices = exo_dir + "choices"
if not os.path.exists(choices):
    os.makedirs(choices)

for i in exo_num:
    imgA = Image.new('RGB', (600, 250), color=(255, 255, 255))
    imgB = Image.new('RGB', (600, 250), color=(255, 255, 255))

    A = ImageDraw.Draw(imgA)
    B = ImageDraw.Draw(imgB)
    sign = ""

    name_imgA = exo_dir + "A{0}.png".format(i)
    if exo[i - 1][0] < exo[i - 1][1]:
        name_imgB = exo_dir + "B{0}-C1.png".format(i)
        sign = "<"
    elif exo[i - 1][0] > exo[i - 1][1]:
        name_imgB = exo_dir + "B{0}-C2.png".format(i)
        sign = ">"
    elif exo[i - 1][0] == exo[i - 1][1]:
        name_imgB = exo_dir + "B{0}-C3.png".format(i)
        sign = "="

    w1, h1 = A.textsize("{0}".format(exo[i - 1][0]), font=fnt1)
    w2, h2 = A.textsize("{0}".format(exo[i - 1][1]), font=fnt1)
    w3, h3 = A.textsize("?", font=fnt1)
    w4, h4 = A.textsize(sign, font=fnt1)

    w0 = 300
    interval = 80

    A.text((w0-interval-w1, 91.108), "{0}".format(exo[i - 1][0]), font=fnt1, fill=(0, 212, 0))
    A.text((w0-(w3/2), 91.285), "?", font=fnt1, fill=(250, 0, 0))
    A.text((w0+interval, 93.698), "{0}".format(exo[i - 1][1]), font=fnt1, fill=(0, 212, 0))

    B.text((w0-interval-w1, 91.108), "{0}".format(exo[i - 1][0]), font=fnt1, fill=(0, 212, 0))
    B.text((w0-(w4/2), 91.285), sign, font=fnt1, fill=(0, 0, 255))
    B.text((w0+interval, 93.698), "{0}".format(exo[i - 1][1]), font=fnt1, fill=(0, 212, 0))

    imgA.save(name_imgA)
    imgB.save(name_imgB)

    print(name_imgA)
    print(name_imgB)


for j in [1, 2, 3]:
    imgC = Image.new('RGB', (120, 80), color=(255, 255, 255))
    C = ImageDraw.Draw(imgC)
    C.text((38.5, 0), answer[j-1], font=fnt2, fill=(0, 0, 255))
    name_imgC = choices + "/C{0}.png".format(j)
    imgC.save(name_imgC)
