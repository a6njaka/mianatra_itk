import os
import re
from collections import defaultdict
import copy


def organize_files(folder_path):
    print("---->>organize_files")
    files = os.listdir(folder_path)
    result = []
    template = {"image1": None, "image2": None, "mp3": [], "answer": None, "text": ""}

    # for file in files:
    #     print(f"-->{file}")

    i = 1
    get_next = True
    while get_next:
        get_next = False
        for file in files:
            match_a = re.search(rf"(A{i})(-.*)*\.(png|jpg)$", file)
            if match_a is not None:
                get_next = True
                result.append(copy.deepcopy(template))
                result[-1]["image1"] = file
                if match_a.group(2) is not None:
                    result[-1]["text"] = match_a.group(2)
                break
        if get_next:
            for file in files:
                match_b = re.search(rf"(B{i})-(.*)\.(png|jpg)$", file)
                if match_b is not None:
                    result[-1]["image2"] = file
                    result[-1]["answer"] = match_b.group(2)
                    break
            for file in files:
                match_c = re.search(rf"(A{i})(-.*)*\.mp3$", file)
                if match_c is not None:
                    result[-1]["mp3"].append(file)
                    break
        i += 1
        # if i == 3:
        #     break

    return result


# Example usage
folder_path = r"D:\Njaka_Project\Njaka_Dev_Itk\bin\Mianatra2\images\dict_mg_v4"
organized_data = organize_files(folder_path)

print("+"*100)
# print(organized_data)
#
for data in organized_data:
    print(data)
print("+"*100)

