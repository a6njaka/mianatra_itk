import random
import lib_template_two_num_ver


def get_image_data(exo_path="", level=3):
    if level <= 0:
        level = 1
    elif level > 4:
        level = 4
    n = random.choice(range(level))
    m = random.choice(range(level))

    a = random.randint(10 ** n, 10 ** (n + 1) - 1)
    b = random.randint(10 ** m, 10 ** (m + 1) - 1)

    return lib_template_two_num_ver.operation2number_vertical(a, b, "+")
