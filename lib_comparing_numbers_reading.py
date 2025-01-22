import lib_number_to_french as french
import random
from PIL import Image, ImageDraw, ImageFont
import copy


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


def get_image_data(level=1):
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
        font_question = ImageFont.truetype("arial.ttf", 25)
        font_expression = ImageFont.truetype("arial.ttf", 70)
        font_reading = ImageFont.truetype("arial.ttf", 50)
    except IOError:
        font_question = ImageFont.load_default()
        font_expression = ImageFont.load_default()
        font_reading = ImageFont.load_default()
    text1_bbox = draw1.textbbox((0, 0), f"{a} {text1} {b}", font=font_expression)
    text2_bbox = draw1.textbbox((0, 0), text2, font=font_reading)

    text1_width, text1_height = text1_bbox[2] - text1_bbox[0], text1_bbox[3] - text1_bbox[1]
    text2_width, text2_height = text2_bbox[2] - text2_bbox[0], text2_bbox[3] - text2_bbox[1]
    txt1_x_start = (854-text1_width)/2
    txt2_x_start = (854-text2_width)/2

    draw1.text((10, 10), "Comment on lit l'expression matheùatique suivant?" , fill=(255, 0, 0), font=font_question)
    draw1.text((txt1_x_start, 160), text1, fill=(0, 100, 0), font=font_expression)
    draw1.text((txt2_x_start, 250), text2, fill=(0, 0, 0), font=font_reading)

    image1.save(r"C:\Users\NJAKA\Desktop\01.png")


    # image2 = Image.new('RGB', (854, 480), color=(220, 220, 220))


get_image_data()

