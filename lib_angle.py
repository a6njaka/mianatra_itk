from PIL import Image, ImageDraw, ImageFont
import random
import math
import copy
import re


def get_image_data(data):
    width = 854
    height = 480
    image1 = Image.new("RGB", (width, height), (200, 200, 200))
    draw1 = ImageDraw.Draw(image1)
    angle = random.randint(3, 18) * 10

    font_size = 30
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
        font_question = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        font = ImageFont.load_default()
        font_question = ImageFont.load_default()

    text = f"{angle}°"

    center_x = width // 2
    center_y = height // 2 + 100

    line_length = 300

    # Base line
    base_end_x = center_x + line_length
    base_end_y = center_y
    draw1.line((center_x, center_y, base_end_x, base_end_y), fill="black", width=3)

    # Angle line
    angle_rad = math.radians(angle)
    angle_end_x = center_x + int(line_length * math.cos(angle_rad))
    angle_end_y = center_y - int(line_length * math.sin(angle_rad))
    draw1.line((center_x, center_y, angle_end_x, angle_end_y), fill="black", width=3)

    # Arc drawing (Corrected)
    radius = 60
    start_angle = -angle
    end_angle = 0

    bbox = (center_x - radius, center_y - radius, center_x + radius, center_y + radius)
    radius_dot = 3
    dot = (center_x - radius_dot, center_y - radius_dot, center_x + radius_dot, center_y + radius_dot)
    draw1.arc(bbox, start=start_angle, end=end_angle, fill="purple", width=3)
    draw1.arc(dot, start=0, end=360, fill="red", width=3)

    # Angle value placement (Corrected and larger font)
    text = f"{angle}°"
    angle_rad_text = math.radians(angle / 2)
    angle_text_x = center_x + int((radius + 40) * math.cos(angle_rad_text))
    angle_text_y = center_y - int((radius + 40) * math.sin(angle_rad_text))

    angle_text_bbox = draw1.textbbox((0, 0), text, font=font)
    angle_text_width = angle_text_bbox[2] - angle_text_bbox[0]
    angle_text_height = angle_text_bbox[3] - angle_text_bbox[1]

    angle_text_x -= angle_text_width // 2
    angle_text_y -= angle_text_height // 2
    draw1.text((15, 15), "Quelle est la valeur de l'angle sur cette image?", fill="blue", font=font_question)

    image2 = copy.deepcopy(image1)
    draw2 = ImageDraw.Draw(image2)

    draw1.text((angle_text_x, angle_text_y), "?", fill="red", font=font)
    draw2.text((angle_text_x, angle_text_y), text, fill="red", font=font)

    angle_str = f"{angle}"
    answer = re.compile(rf"^\s*{re.escape(angle_str)}\s*(°|degrés?|degres?)$")

    return image1, image2, [], answer, f"{angle_str} °"
