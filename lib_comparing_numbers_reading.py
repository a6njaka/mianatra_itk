import lib_number_to_french as french
import random
from PIL import Image, ImageDraw, ImageFont
import copy
import re


def convert_to_phrase(a, b):
    exp_math = ""
    text = ""
    a_text = french.number_to_french(a)
    b_text = french.number_to_french(b)

    if a == b:
        exp_math = f"="
        text = f"{a_text} est égale à {b_text}".capitalize()
    elif a > b:
        exp_math = f">"
        text = f"{a_text} est supérieur à {b_text}".capitalize()
    elif a < b:
        exp_math = f"<"
        text = f"{a_text} est inférieur à {b_text}".capitalize()
    return exp_math, text


def get_image_data(data):
    level = data["level"]
    case_sensitive = data["case sensitive"]
    if level <= 0:
        level = 1
    elif level > 3:
        level = 3
    a = random.randint(0, 10 ** level - 1)
    b = random.randint(0, 10 ** level - 1)

    # Create a blank white image
    image1 = Image.new('RGB', (854, 480), color=(220, 220, 220))
    draw1 = ImageDraw.Draw(image1)

    text1, text2 = convert_to_phrase(a, b)
    # Define font size and load font
    font_size = 40
    try:
        font_question = ImageFont.truetype("arial.ttf", 20)
        font_expression = ImageFont.truetype("arial.ttf", 70)
        font_reading = ImageFont.truetype("arial.ttf", 30)
    except IOError:
        font_question = ImageFont.load_default()
        font_expression = ImageFont.load_default()
        font_reading = ImageFont.load_default()
    text1_bbox = draw1.textbbox((0, 0), f"{text1} ", font=font_expression)
    text_a_bbox = draw1.textbbox((0, 0), f"{a} ", font=font_expression)
    text_b_bbox = draw1.textbbox((0, 0), f"{b}", font=font_expression)
    text2_bbox = draw1.textbbox((0, 0), text2, font=font_reading)

    text1_width, text1_height = text1_bbox[2] - text1_bbox[0], text1_bbox[3] - text1_bbox[1]
    text2_width, text2_height = text2_bbox[2] - text2_bbox[0], text2_bbox[3] - text2_bbox[1]
    text_a_width, text_a_height = text_a_bbox[2] - text_a_bbox[0], text_a_bbox[3] - text_a_bbox[1]
    text_b_width, text_b_height = text_b_bbox[2] - text_b_bbox[0], text_b_bbox[3] - text_b_bbox[1]
    txt1_x_start = (854 - text1_width - text_a_width - text_b_width) / 2
    txt2_x_start = (854 - text2_width) / 2

    draw1.text((15, 20), "Comment lit-on l'expression mathématique suivante?", fill=(255, 0, 0), font=font_question)
    draw1.text((txt1_x_start, 160), f"{a}", fill=(0, 0, 200), font=font_expression)
    draw1.text((txt1_x_start + text_a_width, 160), f"{text1}", fill=(0, 200, 0), font=font_expression)
    draw1.text((txt1_x_start + text_a_width + text1_width, 160), f"{b}", fill=(0, 0, 200), font=font_expression)

    image2 = copy.deepcopy(image1)
    draw2 = ImageDraw.Draw(image2)
    draw1.text((180, 350), "."*60, fill=(255, 0, 0), font=font_reading)
    draw2.text((txt2_x_start, 350), text2, fill=(129, 23, 141), font=font_reading)

    image1.save(r"C:\Users\NJAKA\Desktop\01.png")

    pil_image1 = image1.convert('RGB')
    pil_image2 = image2.convert('RGB')

    image_data1 = pil_image1.tobytes()
    image_data2 = pil_image2.tobytes()

    answer = text2
    if not case_sensitive:
        answer = re.compile(rf"^\s*{re.escape(answer)}\s*$", re.IGNORECASE)
    else:
        answer = re.compile(rf"^\s*{re.escape(answer)}\s*$")
    text = f"{a}{text1}{b}"
    # print(f"{text}: {answer}")
    return image_data1, image_data2, answer, text


data = {"level": 1, "case sensitive": False}
get_image_data(data)
