from PIL import Image, ImageDraw, ImageFont
import random
import os
import re
import copy


def get_image_data(data):
    level = data["level"]
    folder_path = data["folder_path"]
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
        img1 = Image.new('RGB', (854, 480), color=(255, 255, 255))
        draw1 = ImageDraw.Draw(img1)
        font_price = ImageFont.truetype('arial.ttf', 25)
        font_question_mark = ImageFont.truetype('arial.ttf', 25)
        logo_width = 110
        marge = 15
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
            for _ in range(random.randint(2, 4)):
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
        logo_y = 300
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
                draw1.text((x0 - marge + (logo_width + marge) * i, logo_y - 60), "+", font=font_price, fill='black')
            draw1.text((x0 + (logo_width + marge) * i + d, logo_y), price, font=font_price, fill='black')
            i += 1

        draw1.text((x0 - marge + (logo_width + marge) * i, logo_y - 60), "= ?", font=font_price, fill='red')
        font = ImageFont.truetype('arial.ttf', 25)
        draw1.text((20, 10), "Hoatrinona ireo?", font=font, fill='black')
        font_final_price = ImageFont.truetype('arial.ttf', 40)
        img2 = copy.deepcopy(img1)
        draw2 = ImageDraw.Draw(img2)

        draw1.text((350, 400), "............ Ariary", font=font_final_price, fill='red')
        draw2.text((350, 400), f"{final_price} Ariary", font=font_final_price, fill='red')

        pil_image1 = img1.convert('RGB')
        pil_image2 = img2.convert('RGB')

        image_data1 = pil_image1.tobytes()
        image_data2 = pil_image2.tobytes()

        answer = f"{final_price}"
        return image_data1, image_data2, re.compile(rf"^\s*{re.escape(answer)}\s*(Ar|Ariary)?$", re.IGNORECASE), f"{final_price_str}={answer}"
    return None, None, None, None
