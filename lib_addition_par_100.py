import random
import lib_template_two_num_ver


def get_image_data(data):
    level = data["level"]
    if level <= 1:
        level = 1
    elif level > 9:
        level = 9
    a = random.randint(1, 9) * 100
    b = random.randint(1, 9) * 100

    return lib_template_two_num_ver.operation2number_vertical(a, b, "+")
