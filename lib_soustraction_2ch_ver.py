import random
import lib_template_two_num_ver


def get_image_data(data):
    level = data["level"]
    if level <= 0:
        level = 1
    elif level > 4:
        level = 4
    a = random.randint(10 ** level, 10 ** (level + 1))
    b = random.randint(1, 10 ** (level + 1))
    while a <= b:
        b = random.randint(1, 10 ** (level + 1))

    return lib_template_two_num_ver.operation2number_vertical(a, b, "-")
