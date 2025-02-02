from PIL import Image, ImageDraw, ImageFont
import re
import copy
import random


def get_image_data(data):
    # Create a blank white image
    width, height = 854, 480
    image1 = Image.new("RGB", (width, height), color=(230, 230, 230))
    draw1 = ImageDraw.Draw(image1)

    # Load font with size 70
    try:
        font = ImageFont.truetype("arial.ttf", 35)
        font_question = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        font = ImageFont.load_default()
        font_question = ImageFont.load_default()

    # Calculate text dimensions
    # text_length, text_height_a = draw1.textbbox((0, 0), a_str, font=font)[2:]

    length_in_cm = random.randint(4, 15)
    line_length = int(length_in_cm * 854 / 19.2)
    x_start = (854 - line_length) / 2
    x_end = x_start + line_length
    y_line = 280
    d = 20

    draw1.text((15, 15), "Quelle est la longueur du segment AB en cm ?", fill="red", font=font_question)
    draw1.text((854 / 2 + 20, y_line - 45), "cm", fill="blue", font=font)  # Draw a
    draw1.line([(x_start, y_line), (x_end, y_line)], fill="black", width=4)
    draw1.line([(x_start, y_line - d), (x_start, y_line + d)], fill="black", width=4)
    draw1.line([(x_end, y_line - d), (x_end, y_line + d)], fill="black", width=4)
    draw1.text((x_start - 12, y_line - 55), "A", fill="black", font=font)  # Draw a
    draw1.text((x_end - 12, y_line - 55), "B", fill="black", font=font)  # Draw a

    image2 = copy.deepcopy(image1)
    draw2 = ImageDraw.Draw(image2)
    draw1.text((854 / 2 - 70, y_line - 45), "........", fill="red", font=font)  # Draw a
    d = 25
    if len(f"{length_in_cm}") == 1:
        d = 10
    draw2.text((854 / 2 - d, y_line - 45), f"{length_in_cm}", fill="red", font=font)  # Draw a

    pil_image1 = image1.convert('RGB')
    pil_image2 = image2.convert('RGB')

    image_data1 = pil_image1.tobytes()
    image_data2 = pil_image2.tobytes()

    # pil_image2.save(r"C:\Users\NJAKA\Desktop\01.png")

    length_in_cm = f"{length_in_cm}"
    answer = re.compile(rf"^\s*{re.escape(length_in_cm)}\s*(cm|centimètres)$")

    return image_data1, image_data2, [], answer, f"{length_in_cm} cm"


# data = {"level": 3, "case sensitive": False}
# get_image_data(data)
