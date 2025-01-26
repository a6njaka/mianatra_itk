import random
import lib_template_two_num_ver


def get_image_data(data):
    level = data["level"]
    if level <= 1:
        level = 1
    elif level > 9:
        level = 9
    a = random.randint(10 ** (level-1), 10 ** level)
    b = 6

    return lib_template_two_num_ver.operation2number_vertical(a, b, "*")
