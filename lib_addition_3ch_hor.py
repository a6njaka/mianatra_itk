from PIL import Image, ImageDraw, ImageFont
import random
import re


def get_image(level=1):
    a = random.randint(0, 10 ** level - 1)
    b = random.randint(0, 10 ** level - 1)
    c = random.randint(0, 10 ** level - 1)
    answer = a + b + c
    # Create a blank white image
    pil_image = Image.new('RGB', (854, 480), color=(255, 255, 255))

    # Initialize the drawing context
    draw = ImageDraw.Draw(pil_image)

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
    text_bbox = draw.textbbox((0, 0), text, font=font)
    q_bbox = draw.textbbox((0, 0), question_mark, font=font)

    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    q_width, q_height = q_bbox[2] - q_bbox[0], q_bbox[3] - q_bbox[1]

    # Calculate positions for center alignment
    total_width = text_width + q_width
    x_start = (854 - total_width) // 2
    y_start = (480 - text_height) // 2

    # Draw the equation text
    draw.text((x_start, y_start), text, fill=(0, 0, 0), font=font)

    # Draw the question mark in red
    draw.text((x_start + text_width, y_start), question_mark, fill=(255, 0, 0), font=font)

    # Ensure RGB mode for wxPython and convert to bytes
    pil_image = pil_image.convert('RGB')
    image_data = pil_image.tobytes()

    pil_image.save("njk.png")

    # print(type(image_data))

    # TODO: Use regex for the answer

    return image_data, image_data, answer


get_image(5)
