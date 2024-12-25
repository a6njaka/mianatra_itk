from PIL import Image, ImageDraw, ImageFont
import os

exo = [
    [4, 2],
    [1, 5],
    [2, 3],
    [5, 3],
    [4, 5]
]
exo = [
    [3, 3],
    [2, 5],
    [2, 3],
    [5, 5],
    [3, 5]
]

fnt1 = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 70)
fnt2 = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 60)

exo_dir = r"C:/Users/NJAKA/Desktop/math_addition_h/"

if not os.path.exists(exo_dir):
    os.makedirs(exo_dir)
choices = exo_dir + "choices"
if not os.path.exists(choices):
    os.makedirs(choices)
# Rand
f = open(choices + '/rand.txt', 'w')
f.write('rand the choices')
f.close()

for i in range(1, len(exo) + 1):
    imgA = Image.new('RGB', (600, 250), color=(255, 255, 255))
    imgB = Image.new('RGB', (600, 250), color=(255, 255, 255))
    imgC = Image.new('RGB', (120, 80), color=(255, 255, 255))

    A = ImageDraw.Draw(imgA)
    B = ImageDraw.Draw(imgB)
    C = ImageDraw.Draw(imgC)

    name_imgA = exo_dir + "A{0}.png".format(i)
    name_imgB = exo_dir + "B{0}-C{0}.png".format(i)
    name_imgC = choices + "/C{0}.png".format(i)

    w1, h1 = A.textsize("{0}".format(exo[i - 1][0]), font=fnt1)
    w2, h2 = A.textsize("{0}".format(exo[i - 1][1]), font=fnt1)
    w3, h3 = A.textsize("{0}".format(exo[i - 1][0] + exo[i - 1][1]), font=fnt1)
    w4, h4 = A.textsize("{0}".format(exo[i - 1][0] + exo[i - 1][1]), font=fnt2)

    wd = 0
    aad = "{}{}".format(exo[i - 1][0], exo[i - 1][1])
    if len(aad) == 2:
        wd = 20
    elif len(aad) == 3:
        wd = 15
    elif len(aad) == 4:
        wd = 10
    else:
        wd = 5

    xo = 350
    wt, ht = A.textsize("+", font=fnt1)

    print("{}-{}".format(w1, h1))
    print("{}-{}".format(w2, h2))

    A.text((xo - wd - w2, 90), "{0}".format(exo[i - 1][1]), font=fnt1, fill=(0, 12, 200))
    A.text((xo - (wd * 2) - w2 - wt, 90), "+", font=fnt1, fill=(0, 0, 0))
    A.text((xo - (wd * 3) - w2 - w1 - wt, 90), "{0}".format(exo[i - 1][0]), font=fnt1, fill=(0, 12, 200))
    A.text((xo, 90), "=", font=fnt1, fill=(0, 0, 0))
    A.text((410, 90), "?", font=fnt1, fill=(250, 0, 0))

    B.text((xo - wd - w2, 90), "{0}".format(exo[i - 1][1]), font=fnt1, fill=(0, 12, 200))
    B.text((xo - (wd * 2) - w2 - wt, 90), "+", font=fnt1, fill=(0, 0, 0))
    B.text((xo - (wd * 3) - w2 - w1 - wt, 90), "{0}".format(exo[i - 1][0]), font=fnt1, fill=(0, 12, 200))
    B.text((xo, 90), "=", font=fnt1, fill=(0, 0, 0))
    B.text((410, 90), "{0}".format(exo[i - 1][0] + exo[i - 1][1]), font=fnt1, fill=(250, 0, 0))

    C.text(((120 - w4) / 2, ((80 - h4) / 2) - 5), "{0}".format(exo[i - 1][0] + exo[i - 1][1]), font=fnt2, fill=(0, 0, 255))

    print("{0}".format(exo[i - 1][0] + exo[i - 1][1]))

    imgA.save(name_imgA)
    imgB.save(name_imgB)
    imgC.save(name_imgC)

    print(name_imgA)
    print(name_imgB)
