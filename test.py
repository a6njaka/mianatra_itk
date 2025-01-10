from PIL import Image, ImageDraw, ImageFont


def addition2number_vertical(a, b, output_path="addition_result.png"):
    # Create a blank white image
    width, height = 854, 480
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Load font with size 70
    try:
        font = ImageFont.truetype("arial.ttf", 50)  # Use a default font
    except IOError:
        font = ImageFont.load_default()

    # Convert numbers to strings, with "+" added to a and b
    a_str = f"{a}"
    b_str = f"{b}"
    sum_str = str(a + b)

    # Calculate text dimensions
    text_width_a, text_height_a = draw.textbbox((0, 0), a_str, font=font)[2:]
    text_width_b, text_height_b = draw.textbbox((0, 0), b_str, font=font)[2:]
    text_width_sum, text_height_sum = draw.textbbox((0, 0), sum_str, font=font)[2:]

    # Define positions (aligned to the right)
    x_right = 500  # Right margin
    y_start = height // 4

    # Positions for a, b, and sum
    x_a = x_right - text_width_a
    y_a = y_start

    x_b = x_right - text_width_b
    y_b = y_a + text_height_a + 20

    line_y = y_b + text_height_b + 25  # Line below b

    x_sum = x_right - text_width_sum
    y_sum = line_y + 20

    # Draw the text and line
    draw.text((x_a, y_a), a_str, fill="black", font=font)  # Draw a
    draw.text((x_b, y_b), b_str, fill="black", font=font)  # Draw b
    draw.text((x_right - max(text_width_a, text_width_b) - 50, (y_a + y_b) / 2), "+", fill="black", font=font)  # Draw b
    draw.line([(x_right - max(text_width_a, text_width_b) - 21, line_y), (x_right, line_y)], fill="black", width=5)  # Draw line
    draw.text((x_sum, y_sum), sum_str, fill="red", font=font)  # Draw sum in red

    # Save the image
    image.save(output_path)
    print(f"Image saved as {output_path}")


# Example usage
addition2number_vertical(2005, 117)
