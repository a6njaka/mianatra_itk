import lib_number_to_french as french
import random
from PIL import Image, ImageDraw, ImageFont
import copy
import re


def get_image_data(data):
    level = data["level"]
    case_sensitive = data["case sensitive"]
    if level <= 0:
        level = 1
    elif level > 3:
        level = 3
    n = random.randint(0, 10 ** level - 1)
    n_text = french.number_to_french(n).capitalize()

    # Create a blank white image
    image1 = Image.new('RGB', (854, 480), color=(220, 220, 220))
    draw1 = ImageDraw.Draw(image1)

    font_size = 40
    try:
        font_question = ImageFont.truetype("arial.ttf", 20)
        font_number = ImageFont.truetype("arial.ttf", 45)
    except IOError:
        font_question = ImageFont.load_default()
        font_number = ImageFont.load_default()
    number_bbox = draw1.textbbox((0, 0), f"{n} ", font=font_number)
    number_text_bbox = draw1.textbbox((0, 0), f"{n_text} ", font=font_number)

    n_width, n_height = number_bbox[2] - number_bbox[0], number_bbox[3] - number_bbox[1]
    n_number_width, n_number_height = number_text_bbox[2] - number_text_bbox[0], number_text_bbox[3] - number_text_bbox[1]
    n_start = 80
    equal_start = n_start + n_width
    n_number_start = n_start + 50 + n_width

    draw1.text((15, 20), "Comment écrire ce nombre en toutes lettres ?", fill=(255, 0, 0), font=font_question)
    draw1.text((n_start, 200), f"{n}", fill=(0, 0, 0), font=font_number)
    draw1.text((equal_start, 205), f"=", fill=(129, 23, 141), font=font_number)

    image2 = copy.deepcopy(image1)
    draw2 = ImageDraw.Draw(image2)

    draw1.text((n_number_start, 200), "." * 40, fill=(255, 0, 0), font=font_number)
    draw2.text((n_number_start, 200), f"{n_text}", fill=(0, 0, 200), font=font_number)

    # image2.save(r"C:\Users\NJAKA\Desktop\01.png")

    pil_image1 = image1.convert('RGB')
    pil_image2 = image2.convert('RGB')

    image_data1 = pil_image1.tobytes()
    image_data2 = pil_image2.tobytes()

    answer = n_text
    if not case_sensitive:
        answer = re.compile(rf"^\s*{re.escape(answer)}\s*$", re.IGNORECASE)
    else:
        answer = re.compile(rf"^\s*{re.escape(answer)}\s*$")
    text = f"{n}"
    # print(f"{text}: {answer}")
    return image_data1, image_data2, [], answer, text


# data = {"level": 3, "case sensitive": False}
# get_image_data(data)
