from PIL import Image, ImageDraw, ImageFont
import os

exo = [
    [5, 3],
    [4, 5],
    [2, 3],
    [1, 6],
    [4, 2]
]
error = 0
answer = []
for i in range(0, 5):
    sum_ab = exo[i][0] + exo[i][1]
    if sum_ab not in answer:
        exo[i].append(sum_ab)
        answer.append(sum_ab)
        print("{} + {} = {} <--- OK".format(exo[i][0], exo[i][1], exo[i][0] + exo[i][1]))
    else:
        error += 1
        print("{} + {} = {} <--- Sum already exist".format(exo[i][0], exo[i][1], exo[i][0] + exo[i][1]))

if error == 0:
    fnt1 = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 40)
    fnt2 = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 40)

    exo_dir = r"C:/Users/NJAKA/Desktop/math_addition_h/"

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
        w_a, h_a = A.textsize("{0}".format(exo[i - 1][0]), font=fnt1)
        w_b, h_b = A.textsize("{0}".format(exo[i - 1][1]), font=fnt1)
        w_c, h_c = A.textsize("{0}".format(exo[i - 1][0] + exo[i - 1][1]), font=fnt2)

        wd = 0
        aad = "{}{}".format(exo[i - 1][0], exo[i - 1][1])
        if len(aad) == 2:
            wd = 20
            print("{}".format(aad))
        elif len(aad) == 3:
            wd = 20
        elif len(aad) == 4:
            wd = 20
        else:
            wd = 5

        w_sign, h_sign = A.textsize("+", font=fnt1)

        x_center = image_width / 2
        y_center = image_height / 2

        A.text((x_center - wd - w_a, y_center - (h_a / 2)), "{0}".format(exo[i - 1][0]), font=fnt1, fill=(0, 12, 200))
        A.text((x_center - (w_sign / 2), y_center - (h_sign / 2)), "+", font=fnt1, fill=(255, 0, 0))
        A.text((x_center + wd, y_center - (h_b / 2)), "{0}".format(exo[i - 1][1]), font=fnt1, fill=(0, 12, 200))
        B.text((x_center - (w_c / 2), y_center - (h_c / 2)), "{0}".format(exo[i - 1][2]), font=fnt2, fill=(0, 200, 0))

        # print("{0}".format(exo[i - 1][0] + exo[i - 1][1]))

        imgA.save(name_imgA)
        imgB.save(name_imgB)

        print(name_imgA)
        print(name_imgB)
