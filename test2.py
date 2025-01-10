import os
import re
from collections import defaultdict
import copy


def reformat_answer(text):
    result = ""
    n = len(text)
    for i in range(n):
        t = text[i]
        tmp = ""
        if i != n - 1:
            tmp = text[i + 1]
        if tmp != "#" and t != "#":
            result += f"{t}".lower()
        elif t != "#":
            result += f"{t}".upper()
    return result


def organize_files(folder_path):
    print("---->>organize_files")
    files = os.listdir(folder_path)
    result = []
    template = {"image1": None, "image2": None, "mp3": [], "answer": None, "text": ""}

    i = 1
    get_next = True
    while get_next:
        get_next = False
        for file in files:
            match_a = re.search(rf"(A{i})(-.*)*\.(png|jpg)$", file)
            if match_a is not None:
                get_next = True
                result.append(copy.deepcopy(template))
                result[-1]["image1"] = os.path.join(folder_path, file)
                if match_a.group(2) is not None:
                    result[-1]["text"] = match_a.group(2)
                break
        if get_next:
            for file in files:
                match_b = re.search(rf"(B{i})-(.*)\.(png|jpg)$", file)
                if match_b is not None:
                    result[-1]["image2"] = os.path.join(folder_path, file)
                    result[-1]["answer"] = reformat_answer(match_b.group(2))
                    break
            for file in files:
                match_c = re.search(rf"(A{i})(-.*)*\.mp3$", file)
                if match_c is not None:
                    result[-1]["mp3"].append(os.path.join(folder_path, file))
                    break
        i += 1
    return result


# Example usage
folder_path = r"D:\Njaka_Project\Njaka_Dev_Itk\bin\Mianatra2\images\dict_mg_v4"
organized_data = organize_files(folder_path)

print("+" * 100)
# print(organized_data)
#
for data in organized_data:
    print(data)
print("+" * 100)
