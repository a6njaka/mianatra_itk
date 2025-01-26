import random
import lib_template_two_num_ver


def get_image_data(data):
    level = data["level"]
    if level <= 0:
        level = 1
    elif level > 3:
        level = 3
    a = random.randint(10 ** level, 10 ** (level + 1))
    b = random.randint(10 ** (level - 1), 10 ** level - 1)

    return lib_template_two_num_ver.operation2number_vertical(a, b, "-")
