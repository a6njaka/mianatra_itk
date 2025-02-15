import base64


image = r"C:\Users\NJAKA\Desktop\istockphoto-597276512-612x612 - Copie.jpg"
image = r"C:\Users\NJAKA\Desktop\Montre_exo.png"
with open(image, "rb") as image_file:
    base64_string = base64.b64encode(image_file.read()).decode("utf-8")

print(base64_string)
