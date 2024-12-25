from PIL import Image, ImageDraw, ImageFont
import os

exo = [
    [5, 2],
    [1, 5],
    [2, 3],
    [5, 3],
    [4, 5]
]
exo = [
    [2, 1],
    [3, 2],
    [6, 1],
    [2, 4],
    [4, 4]
]
exo_num = [1, 2, 3, 4, 5]
answer = ["<", ">", "="]

fnt1 = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 70)
fnt2 = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 60)

exo_dir = r"C:/Users/NJAKA/Desktop/math_addition_v/"

if not os.path.exists(exo_dir):
    os.makedirs(exo_dir)
choices = exo_dir + "choices"
if not os.path.exists(choices):
    os.makedirs(choices)
# Rand
f = open(choices + '/rand.txt', 'w')
f.write('rand the choices')
f.close()

for i in exo_num:
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

    A.text((330 - w1, 12), "{0}".format(exo[i - 1][0]), font=fnt1, fill=(0, 212, 0))
    A.text((230, 60), "+", font=fnt1, fill=(250, 0, 0))
    A.text((330 - w2, 90), "{0}".format(exo[i - 1][1]), font=fnt1, fill=(0, 212, 0))
    A.text((245, 95), "___", font=fnt1, fill=(0, 0, 0))
    A.text((285, 170), "?", font=fnt1, fill=(250, 0, 0))

    B.text((330 - w1, 12), "{0}".format(exo[i - 1][0]), font=fnt1, fill=(0, 212, 0))
    B.text((230, 60), "+", font=fnt1, fill=(250, 0, 0))
    B.text((330 - w2, 90), "{0}".format(exo[i - 1][1]), font=fnt1, fill=(0, 212, 0))
    B.text((245, 95), "___", font=fnt1, fill=(0, 0, 0))
    B.text((330 - w3, 170), "{0}".format(exo[i - 1][0] + exo[i - 1][1]), font=fnt1, fill=(255, 0, 0))

    C.text(((120 - w4) / 2, ((80 - h4) / 2) - 5), "{0}".format(exo[i - 1][0] + exo[i - 1][1]), font=fnt2, fill=(0, 0, 255))

    print("{0}".format(exo[i - 1][0] + exo[i - 1][1]))

    imgA.save(name_imgA)
    imgB.save(name_imgB)
    imgC.save(name_imgC)

    print(name_imgA)
    print(name_imgB)
