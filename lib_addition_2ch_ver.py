import random
import lib_template_two_num_ver


def get_image_data(exo_path="", level=3):
    a = random.randint(0, 10 ** level - 1)
    b = random.randint(0, 10 ** level - 1)

    return lib_template_two_num_ver.operation2number_vertical(a, b, "+")
