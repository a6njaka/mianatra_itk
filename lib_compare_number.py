from PIL import Image, ImageDraw, ImageFont
import random
import re
import copy


def get_image_data(data):
    level = data["level"]
    if level <= 1:
        level = 1
    elif level > 7:
        level = 7
    a = random.randint(0, 10 ** level)
    b = random.randint(0, 10 ** level)

    width, height = 854, 480
    image1 = Image.new('RGB', (width, height), color='white')
    image2 = Image.new('RGB', (width, height), color='white')
    draw1 = ImageDraw.Draw(image1)
    draw2 = ImageDraw.Draw(image2)

    try:
        font = ImageFont.truetype("arial.ttf", 60)
    except IOError:
        font = ImageFont.load_default()

    a_width = draw1.textbbox((0, 0), f"{a}", font=font)[2]
    b_width = draw1.textbbox((0, 0), f"{a}", font=font)[2]
    compare_width = draw1.textbbox((0, 0), "...", font=font)[2]

    # Calculate the total width of the full text
    total_text_width = a_width + b_width + compare_width

    # Calculate starting position to center the text
    w_separator = 20
    start_x = (width - total_text_width - w_separator * 2) // 2
    text_y = (height - draw1.textbbox((0, 0), f"{a}", font=font)[3]) // 2

    x_a = start_x
    x_compare = start_x + a_width + w_separator
    x_b = x_compare + compare_width + w_separator

    draw1.text((x_a, text_y), f"{a}", fill=(0, 0, 0), font=font)
    draw1.text((x_compare, text_y), f"...", fill=(255, 0, 0), font=font)
    draw1.text((x_b, text_y), f"{b}", fill=(0, 0, 0), font=font)

    sign = ""
    answer = re.compile(rf"^\s*$")
    if a<b:
        sign = "<"
        answer = re.compile(rf"^\s*C1\s*$")
    elif a == b:
        sign = "="
        answer = re.compile(rf"^\s*C2\s*$")
    else:
        sign = ">"
        answer = re.compile(rf"^\s*C3\s*$")

    draw1.text((x_a, text_y), f"{a}", fill=(0, 0, 0), font=font)
    draw1.text((x_compare, text_y), f"...", fill=(255, 0, 0), font=font)
    draw1.text((x_b, text_y), f"{b}", fill=(0, 0, 0), font=font)

    draw2.text((x_a, text_y), f"{a}", fill=(0, 0, 0), font=font)
    draw2.text((x_compare, text_y), sign, fill=(255, 0, 0), font=font)
    draw2.text((x_b, text_y), f"{b}", fill=(0, 0, 0), font=font)

    pil_image1 = image1.convert('RGB')
    pil_image2 = image2.convert('RGB')

    image_data1 = pil_image1.tobytes()
    image_data2 = pil_image2.tobytes()

    text = f"{a} vs {b}|{a}<{b}\t{a}={b}\t{a}>{b}"
    choices = [image_text_center1("<"), image_text_center1("="), image_text_center1(">")]

    return image_data1, image_data2, choices, answer, text


def image_text_center1(text, size=(120, 80), font_size=80):
    width, height = size
    image1 = Image.new('RGB', (width, height), color=(184, 239, 201))
    draw1 = ImageDraw.Draw(image1)

    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    draw1.text((35, -5), text, font=font, fill=(166, 15, 223))
    pil_image1 = image1.convert('RGB')

    return pil_image1


def image_text_center2(text, size=(854, 480), font_size=50):
    width, height = size
    image = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), text, font=font)  # Note the change here
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    start_x = (width - text_width) / 2
    start_y = (height - text_height) / 2

    draw.text((start_x, start_y), text, font=font, fill=(0, 0, 0))

    pil_image = image.convert('RGB')

    image_data = pil_image.tobytes()
    return image_data

