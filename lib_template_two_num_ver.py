from PIL import Image, ImageDraw, ImageFont
import re


def operation2number_vertical(a, b, operation="+"):
    # Create a blank white image
    width, height = 854, 480
    image1 = Image.new("RGB", (width, height), color=(230, 230, 230))
    image2 = Image.new("RGB", (width, height), color=(230, 230, 230))
    draw1 = ImageDraw.Draw(image1)
    draw2 = ImageDraw.Draw(image2)

    # Load font with size 70
    try:
        font = ImageFont.truetype("arial.ttf", 70)  # Use a default font
    except IOError:
        font = ImageFont.load_default()

    # Convert numbers to strings, with "+" added to a and b
    a_str = f"{a}"
    b_str = f"{b}"
    result = 0
    if operation == "+":
        result = str(a + b)
    elif operation == "-":
        result = str(a - b)
    elif operation.lower() == "x" or operation.lower() == "*":
        result = str(a * b)
        operation = "x"

    # Calculate text dimensions
    text_width_a, text_height_a = draw1.textbbox((0, 0), a_str, font=font)[2:]
    text_width_b, text_height_b = draw1.textbbox((0, 0), b_str, font=font)[2:]
    text_width_sum, text_height_sum = draw1.textbbox((0, 0), result, font=font)[2:]

    # Define positions (aligned to the right)
    m = max(text_width_a, text_width_b)

    x_right = (width - m)/2 + m  # Right margin
    y_start = height // 4

    # Positions for a, b, and sum
    x_a = x_right - text_width_a
    y_a = y_start

    x_b = x_right - text_width_b
    y_b = y_a + text_height_a + 10

    line_y = y_b + text_height_b + 25  # Line below b

    x_sum = x_right - text_width_sum
    y_sum = line_y + 10

    # Draw the text and line
    draw1.text((x_a, y_a), a_str, fill="black", font=font)  # Draw a
    draw2.text((x_a, y_a), a_str, fill="black", font=font)  # Draw a

    draw1.text((x_b, y_b), b_str, fill="black", font=font)  # Draw b
    draw2.text((x_b, y_b), b_str, fill="black", font=font)  # Draw b

    draw1.text((x_right - max(text_width_a, text_width_b) - 50, (y_a + y_b) / 2), operation, fill="black", font=font)  # Draw b
    draw2.text((x_right - max(text_width_a, text_width_b) - 50, (y_a + y_b) / 2), operation, fill="black", font=font)  # Draw b

    draw1.line([(x_right - max(text_width_a, text_width_b) - 21, line_y), (x_right, line_y)], fill="black", width=5)  # Draw line
    draw2.line([(x_right - max(text_width_a, text_width_b) - 21, line_y), (x_right, line_y)], fill="black", width=5)  # Draw line

    draw1.text((x_sum, y_sum), "." * int(len(f"{result}")*2), fill="red", font=font)  # Draw sum in red
    draw2.text((x_sum, y_sum), result, fill="red", font=font)  # Draw sum in red

    pil_image1 = image1.convert('RGB')
    pil_image2 = image2.convert('RGB')

    answer = f"{result}"
    return pil_image1, pil_image2, [], [], re.compile(rf"^\s*0*{re.escape(answer)}\s*$"), f"{a}{operation}{b}={result}"


# operation2number_vertical(123, 44, operation="*")
