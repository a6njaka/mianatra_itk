from PIL import Image, ImageDraw, ImageFont
import random
import re
import copy


def get_image_data(data):
    level = data["level"]
    if level <= 3:
        level = 3
    elif level > 7:
        level = 7
    random_number_list = []
    i = 0
    while i < level:
        n = random.randint(1, 9)
        while n in random_number_list:
            n = random.randint(1, 9)
        random_number_list.append(n)
        i += 1

    width, height = 854, 480
    image1 = Image.new('RGB', (width, height), color='white')
    image2 = Image.new('RGB', (width, height), color='white')
    draw1 = ImageDraw.Draw(image1)
    draw2 = ImageDraw.Draw(image2)

    # Set the font for drawing text
    try:
        font_question = ImageFont.truetype("arial.ttf", 20)
        font = ImageFont.truetype("arial.ttf", 50)
    except IOError:
        font_question = ImageFont.load_default()
        font = ImageFont.load_default()

    # Prepare the formatted text with " - " as the separator
    separator = " - "
    min_value = min(random_number_list)  # Find the minimum value
    min_value_str = str(min_value)

    # Reconstruct the text around the minimum value
    text_parts = []
    for num in random_number_list:
        if num == min_value:
            text_parts.append(f"<{num}>")  # Mark the minimum value with tags
        else:
            text_parts.append(str(num))

    # Join the parts with separators
    formatted_text = separator.join(text_parts)

    # Replace the tags for splitting into parts
    before_text, min_text, after_text = formatted_text.partition(f"<{min_value}>")
    min_text = min_text.strip("<>")  # Remove the tags from the min value

    # Fix separators around the minimum value
    if before_text.endswith(separator):
        before_text = before_text[:-len(separator)]  # Remove trailing separator
    if after_text.startswith(separator):
        after_text = after_text[len(separator):]  # Remove leading separator

    # Calculate the widths of the text parts
    before_width = draw1.textbbox((0, 0), before_text + (separator if before_text else ""), font=font)[2]
    min_width = draw1.textbbox((0, 0), min_text, font=font)[2]
    after_width = draw1.textbbox((0, 0), (separator if after_text else "") + after_text, font=font)[2]

    # Calculate the total width of the full text
    total_text_width = before_width + min_width + after_width

    # Calculate starting position to center the text
    start_x = (width - total_text_width) // 2
    text_y = (height - draw1.textbbox((0, 0), min_text, font=font)[3]) // 2

    # Draw the text parts
    draw1.text((15, 20), "Quel est le plus petit nombre ?", fill=(255, 0, 0), font=font_question)
    draw2.text((15, 20), "Quel est le plus petit nombre ?", fill=(255, 0, 0), font=font_question)
    if before_text:
        draw1.text((start_x, text_y), before_text + separator, font=font, fill='black')
        draw2.text((start_x, text_y), before_text + separator, font=font, fill='black')
    draw1.text((start_x + before_width, text_y), min_text, font=font, fill='black')
    draw2.text((start_x + before_width, text_y), min_text, font=font, fill='red')
    if after_text:
        draw1.text((start_x + before_width + min_width, text_y), separator + after_text, font=font, fill='black')
        draw2.text((start_x + before_width + min_width, text_y), separator + after_text, font=font, fill='black')

    pil_image1 = image1.convert('RGB')
    pil_image2 = image2.convert('RGB')

    image_data1 = pil_image1.tobytes()
    image_data2 = pil_image2.tobytes()

    answer = re.compile(rf"^\s*{re.escape(min_value_str)}\s*$")
    text = "-".join(map(str, random_number_list))

    return image_data1, image_data2, answer, text


# data = {"level": 3}
# get_image_data(data)
