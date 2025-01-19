from PIL import Image, ImageDraw, ImageFont
import random
import os
import re


def create_image(folder_path, level=1):
    folder_path = os.path.join(folder_path, "source_images")
    all_image = []
    for filename in os.listdir(folder_path):
        if re.search("\\.(png|jpg)", filename, re.IGNORECASE):
            print(filename)
            m = re.search("(.*?)-(\\d+)\\.(png|jpg)$", filename)
            if m is not None:
                all_image.append({
                    "image path": os.path.join(folder_path, filename),
                    "article": m.group(1),
                    "price": m.group(2)}
                )
    img = Image.new('RGB', (854, 480), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    font_price = ImageFont.truetype('arial.ttf', 25)
    logo_width = 134
    marge = 1
    n = len(all_image)
    x0 = int((854 - (logo_width * n + marge * (n - 1))) / 2)
    i = 0
    for images in all_image:
        max_article_number = 6
        a = random.randint(0, max_article_number)
        img_entana = Image.open(images["image path"])
        aspect_ratio = img_entana.width / img_entana.height
        logo_height = int(logo_width / aspect_ratio)
        img_entana = img_entana.resize((logo_width, logo_height))
        logo_y = 300
        price = images["price"]
        price = f"{price} Ar"
        img.paste(img_entana, (x0 + (logo_width + marge) * i, logo_y - logo_height))
        text_bbox = draw.textbbox((0, 0), price, font=font_price)
        text_width = text_bbox[2] - text_bbox[0]  # Right - Left
        text_height = text_bbox[3] - text_bbox[1]  # Bottom - Top
        d = (logo_width - text_width) / 2
        draw.text((x0 + (logo_width + marge) * i + d, logo_y), price, font=font_price, fill='black')
        i += 1

    font = ImageFont.truetype('arial.ttf', 25)  # Replace 'arial.ttf' with your desired font path
    draw.text((20, 10), "Hoatrinona ireo?", font=font, fill='black')
    draw.text((350, 400), "............ Ariary", font=font, fill='red')

    # Save the image
    img.save(r"C:\Users\NJAKA\Desktop\entana.png")


if __name__ == "__main__":
    create_image(r"D:\Njaka_Project\Njaka_Dev_Itk\bin\Mianatra2\images\entana_vidiny")

# pyinstaller -w -F Mianatra2.py
