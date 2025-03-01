from PIL import Image, ImageDraw, ImageFont
import random
import os
import re
import copy


def get_image_data(data):
    level = data["level"]
    folder_path = data["folder_path"]
    folder_vola = data["folder_path"]
    folder_path = os.path.join(folder_path, "source_images")
    all_image = []
    if os.path.isdir(folder_path):
        for filename in os.listdir(folder_path):
            if re.search("\\.(png|jpg)", filename, re.IGNORECASE):
                # print(filename)
                m = re.search("(.*?)-(\\d+)\\.(png|jpg)$", filename)
                if m is not None:
                    all_image.append({
                        "image path": os.path.join(folder_path, filename),
                        "article": m.group(1),
                        "price": m.group(2)}
                    )
        width, height = 1200, 480

        img1 = Image.new('RGB', (width, height), color=(255, 255, 255))
        draw1 = ImageDraw.Draw(img1)
        font_price = ImageFont.truetype('arial.ttf', 25)
        font_question_mark = ImageFont.truetype('arial.ttf', 25)
        logo_width = 150
        marge = 0
        n = len(all_image)
        i = 0
        final_price = 0
        final_price_str = ""

        exo_image_list = []
        if level == 0:
            level = 1
        elif level > 3:
            level = 3
        if level == 1:
            index = random.randint(0, n - 1)
            for _ in range(random.randint(1, 3)):
                exo_image_list.append(all_image[index])
        elif level == 2:
            index1 = random.randint(0, n - 1)
            index2 = random.randint(0, n - 1)
            while index1 == index2:
                index2 = random.randint(0, n - 1)
            a = random.randint(1, 2)
            b = random.randint(1, 4 - a)
            for _ in range(a):
                exo_image_list.append(all_image[index1])
            for _ in range(b):
                exo_image_list.append(all_image[index2])
        elif level == 3:
            print("*" * 100)
            index1 = random.randint(0, n - 1)
            index2 = random.randint(0, n - 1)
            index3 = random.randint(0, n - 1)
            while index1 == index2:
                index2 = random.randint(0, n - 1)
            while index3 == index1 and index3 == index2:
                index3 = random.randint(0, n - 1)
            a = random.randint(1, 2)
            b = random.randint(1, 2)
            c = random.randint(1, 2)
            for _ in range(a):
                exo_image_list.append(all_image[index1])
            for _ in range(b):
                exo_image_list.append(all_image[index2])
            for _ in range(c):
                exo_image_list.append(all_image[index3])
        m = len(exo_image_list)
        x0 = int((854 - (logo_width * m + marge * (m - 1))) / 2)

        x0 = 580
        logo_y = 300
        font_final_price = ImageFont.truetype('arial.ttf', 40)
        draw1.text((x0, logo_y - 80), "-", font=font_final_price, fill='red')
        x0 += 25
        for images in exo_image_list:
            max_article_number = 6
            a = random.randint(0, max_article_number)
            img_entana = Image.open(images["image path"])
            aspect_ratio = img_entana.width / img_entana.height
            logo_height = int(logo_width / aspect_ratio)
            img_entana = img_entana.resize((logo_width, logo_height))
            price = images["price"]
            final_price += int(price)
            if i == 0:
                final_price_str += f"{price}"
            else:
                final_price_str += f"+{price}"
            price = f"{price} Ar"
            img1.paste(img_entana, (x0 + (logo_width + marge) * i, logo_y - logo_height))
            text_bbox = draw1.textbbox((0, 0), price, font=font_price)
            text_width = text_bbox[2] - text_bbox[0]  # Right - Left
            text_height = text_bbox[3] - text_bbox[1]  # Bottom - Top
            d = (logo_width - text_width) / 2
            if i > 0:
                draw1.text((x0 - marge + (logo_width + marge) * i, logo_y - 60), "", font=font_price, fill='black')
            draw1.text((x0 + (logo_width + marge) * i + d, logo_y), price, font=font_price, fill='black')
            i += 1

        draw1.text((x0 - marge + (logo_width + marge) * i, logo_y - 60), "", font=font_price, fill='red')
        font = ImageFont.truetype('arial.ttf', 25)
        draw1.text((20, 10), "Hoatrinona ny famerimbola?", font=font, fill='black')

        # Insert vola image
        vola_rehetra = [5000, 2000, 1000, 500]
        tmp_vola = []
        for v in vola_rehetra:
            if v > final_price:
                tmp_vola.append(v)
        r = random.randint(0, len(tmp_vola)-1)
        vola_noentina = tmp_vola[r]
        vola_noentina_image = os.path.join(folder_vola, "vola", f"{vola_noentina}.jpg")
        if os.path.isfile(vola_noentina_image):
            vola_width = 500
            img_vola = Image.open(vola_noentina_image)
            aspect_ratio = img_vola.width / img_vola.height
            logo_height = int(vola_width / aspect_ratio)
            img_vola = img_vola.resize((vola_width, logo_height))
            img1.paste(img_vola, (60, 100))
        else:
            print(vola_noentina_image)

        img2 = copy.deepcopy(img1)
        draw2 = ImageDraw.Draw(img2)

        answer = f"{vola_noentina-final_price}"
        draw1.text((350, 400), "Famerimbola = ............ Ariary", font=font_final_price, fill='blue')
        draw2.text((350, 400), f"Famerimbola = {answer} Ariary", font=font_final_price, fill='blue')

        pil_image1 = img1.convert('RGB')
        pil_image2 = img2.convert('RGB')

        # pil_image1.save(r"C:\Users\NJAKA\Desktop\01.jpg")

        print(answer)
        return pil_image1, pil_image2, [], [], re.compile(rf"^\s*0*{re.escape(answer)}\s*(Ar|Ariary)?$", re.IGNORECASE), f"{vola_noentina}-({final_price_str})={answer}"
    return None, None, None, None, None


# data0 = {
#     "level": 1,
#     "folder_path": r"C:\Users\NJAKA\Desktop\Raw images\exo"
# }
#
# get_image_data(data0)
