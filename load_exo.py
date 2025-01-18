import json
import random
import lib_addition_3ch_hor
import lib_addition_2ch_ver
from datetime import date
import os
import re
import sys
import copy


class ExoSchedule:
    def __init__(self):
        # self.exo_dir = r"C:\Users\NJAKA\Desktop\exo_itk"
        self.exo_dir = r"D:\Njaka_Project\Njaka_Dev_Itk\bin\Mianatra2\images"
        self.exo_schedule = "exo_schedule.json"
        self.all_exo = {}
        self.load_all_exo()
        self.update_all_exo()

    @staticmethod
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

    def organize_files(self, folder_path, data):
        # print("---->>organize_files")
        files = os.listdir(folder_path)
        result = []
        template = {"image1": "", "image2": "", "mp3": [], "answer": re.compile(""), "text": ""}
        case_sensitive = False
        if data["case sensitive"]:
            case_sensitive = True

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
                    match_b = re.search(rf"(B{i})-(.*)\.(png|jpg)$", file, re.IGNORECASE)
                    if match_b is not None:
                        result[-1]["image2"] = os.path.join(folder_path, file)
                        tmp = rf"{self.reformat_answer(match_b.group(2))}"
                        if case_sensitive:
                            result[-1]["answer"] = re.compile(rf"^{re.escape(tmp)}$")
                            # print(f"    -1->>case_sensitive = {case_sensitive}")
                        else:
                            result[-1]["answer"] = re.compile(rf"^{re.escape(tmp)}$", re.IGNORECASE)
                            # print(f"    -2->>case_sensitive = {case_sensitive}")
                        break
                for file in files:
                    match_c = re.search(rf"(A{i})(-.*)*\.mp3$", file)
                    if match_c is not None:
                        result[-1]["mp3"].append(os.path.join(folder_path, file))
                        break
            i += 1
        return result

    @staticmethod
    def get_today_weekday():
        today = date.today()
        weekday = today.weekday()  # 0 (Monday) to 6 (Sunday)

        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return weekdays[weekday]

    def load_all_exo(self):
        today_weekday = self.get_today_weekday()
        # print(f"--aaa-->>>{self.exo_schedule}")
        with open(self.exo_schedule) as json_file:
            data = json.load(json_file)
            for schedule in data['Itokiana']:
                # print("-->",schedule["exo_number"])
                if today_weekday in schedule['exo_weekdays']:
                    n = min(len(schedule['exo_group']), schedule['exo_number'])
                    random_values = random.sample(schedule['exo_group'], n)
                    for exo in random_values:
                        self.all_exo[exo] = {}

    def display_all_exo(self):
        for exo in self.all_exo:
            print(f"{exo}-->{self.all_exo[exo]}")

    def update_all_exo(self):
        for exo in self.all_exo:
            exo_path = os.path.join(self.exo_dir, exo)
            json_config_path = os.path.join(self.exo_dir, exo, "config.json")
            if os.path.isfile(json_config_path):
                with open(json_config_path) as json_file:
                    data = json.load(json_file)
                    try:
                        self.all_exo[exo]["exo"] = []
                        self.all_exo[exo]["min"] = int(data["min"])
                        self.all_exo[exo]["max"] = int(data["max"])
                        self.all_exo[exo]["level"] = data["level"]
                        self.all_exo[exo]["rand"] = data["rand"]
                        self.all_exo[exo]["type"] = data["type"]
                        self.all_exo[exo]["case sensitive"] = data["case sensitive"]
                        self.all_exo[exo]["comment"] = data["comment"]

                        # if exo == "addition_3ch_hor" or exo == "addition_1":
                        if f"lib_{exo}" in sys.modules:
                            library = sys.modules[f"lib_{exo}"]
                            for _ in range(int(data["max"])):
                                image1, image2, answer, text = library.get_image_data(data["level"])
                                exo_tmp = {
                                    "image1": image1,
                                    "image2": image2,
                                    "mp3": [],
                                    "answer": answer,
                                    "text": text
                                }
                                self.all_exo[exo]["exo"].append(exo_tmp)
                        elif data["type"] == "entry":
                            for exo_tmp in self.organize_files(exo_path, data):
                                self.all_exo[exo]["exo"].append(exo_tmp)
                    except KeyError:
                        self.all_exo[exo] = {}
                        print("Error 12")

# p1 = ExoSchedule()
# p1.display_all_exo()
# TODO:
# - Fix issue Number exo vs Min allowed
# - Improve entry exo
# - Crete exo from lib
# - Implement chose exo
# - Settings for schedule from UI
# - Settings for exo from UI DIALOG
# - Invent management
# - Dashboard

# EXO
#

