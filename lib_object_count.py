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
        width, height = 1100, 480
        img1 = Image.new('RGB', (width, height), color=(255, 255, 255))
        draw1 = ImageDraw.Draw(img1)
        font_price = ImageFont.truetype('arial.ttf', 25)
        font_question_mark = ImageFont.truetype('arial.ttf', 25)
        logo_width = 90
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

        for _ in range(10 * level):
            index = random.randint(0, n - 1)
            exo_image_list.append(all_image[index])

        m = len(exo_image_list)
        x0 = int((width - (logo_width * m + marge * (m - 1))) / 2)
        logo_y = 300
        for i in range(len(exo_image_list)):
            images = exo_image_list[i]
            print(images)
            max_article_number = 6
            a = random.randint(0, max_article_number)
            img_entana = Image.open(images["image path"])
            aspect_ratio = img_entana.width / img_entana.height
            logo_height = int(logo_width / aspect_ratio)
            img_entana = img_entana.resize((logo_width, logo_height))
            price = images["price"]
            final_price += int(price)
            img1.paste(img_entana, (x0 + (logo_width + marge) * i, logo_y - logo_height))
            i += 1

        font = ImageFont.truetype('arial.ttf', 25)
        draw1.text((20, 10), "Firy ny isan'ny ... ?", font=font, fill='black')
        font_final_price = ImageFont.truetype('arial.ttf', 40)
        img2 = copy.deepcopy(img1)
        draw2 = ImageDraw.Draw(img2)

        image_data1 = img1.convert('RGB')
        image_data2 = img2.convert('RGB')

        image_data1.save(r"C:\Users\NJAKA\Desktop\01.jpg")
        print("OK")

        answer = f"{final_price}"
        return image_data1, image_data2, [], re.compile(rf"^\s*{re.escape(answer)}\s*(Ar|Ariary)?$", re.IGNORECASE), f"{final_price_str}={answer}"
    else:
        print("Folder not correct")
        print(folder_path)
    return None, None, None, None, None


os.chdir(r"D:\Njaka_Project\Njaka_Dev_Itk\bin\Mianatra2\images")
data = {
    "level": 1,
    "folder_path": r"mividy_voankazo"
}

get_image_data(data)
