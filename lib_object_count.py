from PIL import Image, ImageDraw, ImageFont
import random
import os
import re
import copy


def get_image_data(data):
    level = data["level"]
    folder_path = data["folder_path"]
    # folder_path = os.path.join(folder_path, "source_images")
    all_image = []
    if os.path.isdir(folder_path):
        for filename in os.listdir(folder_path):
            if re.search("\\.(png|jpg)", filename, re.IGNORECASE):
                # print(filename)
                m = re.search("(.*?)\\.(png|jpg)$", filename)
                if m is not None and os.path.isfile(os.path.join(folder_path,f"{m.group(1)}.mp3")):
                    all_image.append({
                        "image path": os.path.join(folder_path, filename),
                        "mp3": os.path.join(folder_path,f"{m.group(1)}.mp3"),
                        "article name": f"{m.group(1)}",
                    }
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

        if n >= 2:
            for _ in range(10 * level):
                index = random.randint(0, n - 1)
                exo_image_list.append(all_image[index])

            m = len(exo_image_list)
            image_per_col = 10
            x0 = int((width - (logo_width * image_per_col + marge * (image_per_col - 1))) / 2)
            y = 250 if m <= image_per_col else 240
            index_question = random.randint(0, m - 1)
            mp3_question = exo_image_list[index_question]["mp3"]
            image_question = exo_image_list[index_question]["image path"]
            article_name = exo_image_list[index_question]["article name"]

            answer = 0
            for k in range(m):
                images = exo_image_list[i]
                h = 0 if k < 10 else 150
                max_article_number = 6
                a = random.randint(0, max_article_number)
                img_entana = Image.open(images["image path"])
                aspect_ratio = img_entana.width / img_entana.height
                logo_height = int(logo_width / aspect_ratio)
                img_entana = img_entana.resize((logo_width, logo_height))
                img1.paste(img_entana, (x0 + (logo_width + marge) * (k % 10), y - logo_height + h))
                if image_question == images["image path"]:
                    answer += 1
                i += 1

            # print(f"-->{image_question}")
            # print(f"-->{answer}")

            font = ImageFont.truetype('arial.ttf', 25)
            draw1.text((20, 10), f"Firy ny isan'ny {article_name}?", font=font, fill='black')
            font_final_price = ImageFont.truetype('arial.ttf', 40)
            img2 = copy.deepcopy(img1)
            draw2 = ImageDraw.Draw(img2)

            image_data1 = img1.convert('RGB')
            image_data2 = img2.convert('RGB')

            # image_data1.save(r"C:\Users\NJAKA\Desktop\01.jpg")

            answer = f"{answer}"
            return image_data1, image_data2, [], [mp3_question], re.compile(rf"^\s*0*{re.escape(answer)}\s*$", re.IGNORECASE), f"{article_name}={answer}"
    else:
        print("Folder not correct")
        print(folder_path)
    return None, None, None, None, None


# os.chdir(r"D:\Njaka_Project\Njaka_Dev_Itk\bin\Mianatra2\images")
# data = {
#     "level": 2,
#     "folder_path": r"count_object"
# }
#
# get_image_data(data)
