from PIL import Image, ImageDraw, ImageFont
import random
import re


def get_image_data(exo_path="", level=1):
    if level <= 0:
        level = 1
    elif level > 3:
        level = 3
    a = random.randint(0, 10 ** level - 1)
    b = random.randint(0, 10 ** level - 1)
    c = random.randint(0, 10 ** level - 1)
    answer = a + b + c
    # Create a blank white image
    image1 = Image.new('RGB', (854, 480), color=(220, 220, 220))
    image2 = Image.new('RGB', (854, 480), color=(220, 220, 220))

    # Initialize the drawing context
    draw1 = ImageDraw.Draw(image1)
    draw2 = ImageDraw.Draw(image2)

    # Define font size and load font
    font_size = 70
    try:
        font = ImageFont.truetype("arial.ttf", font_size)  # Use Arial font
    except IOError:
        font = ImageFont.load_default()  # Fallback if Arial is unavailable

    # Construct the text
    text = f"{a} + {b} + {c} ="
    question_mark = " ?"

    # Calculate text positions using textbbox
    text_bbox = draw1.textbbox((0, 0), text, font=font)
    q_bbox = draw1.textbbox((0, 0), question_mark, font=font)

    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    q_width, q_height = q_bbox[2] - q_bbox[0], q_bbox[3] - q_bbox[1]

    # Calculate positions for center alignment
    total_width = text_width + q_width
    x_start = (854 - total_width) // 2
    y_start = (480 - text_height) // 2

    # Draw the equation text
    draw1.text((x_start, y_start), text, fill=(0, 0, 0), font=font)
    draw2.text((x_start, y_start), text, fill=(0, 0, 0), font=font)

    # Draw the question mark in red
    draw1.text((x_start + text_width, y_start), question_mark, fill=(255, 0, 0), font=font)
    draw2.text((x_start + text_width, y_start), f" {answer}", fill=(255, 0, 0), font=font)

    # Ensure RGB mode for wxPython and convert to bytes
    pil_image1 = image1.convert('RGB')
    pil_image2 = image2.convert('RGB')

    image_data1 = pil_image1
    image_data2 = pil_image2

    # TODO: Use regex for the answer
    answer = f"{answer}"
    return image_data1, image_data2, [], [], re.compile(rf"^\s*{re.escape(answer)}\s*$"), f"{a}+{b}+{c}={a + b + c}"
