import json
import random
import lib_addition_3ch_hor
import lib_addition_2ch_ver
import lib_mividy_voankazo
import lib_comparing_numbers_reading
import lib_read_number_fr
import lib_line_length
import lib_soustraction_2ch_ver
import lib_multiplication_par_2_ver
import lib_multiplication_par_3_ver
import lib_multiplication_par_4_ver
import lib_multiplication_par_5_ver
import lib_multiplication_par_6_ver
import lib_multiplication_par_7_ver
import lib_multiplication_par_8_ver
import lib_multiplication_par_9_ver
import lib_smallest_number_under_100
import lib_smallest_number_under_10
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
        template = {"image1": "", "image2": "", "choices": [], "mp3": [], "answer": re.compile(""), "text": ""}
        case_sensitive = False
        if data["case sensitive"]:
            case_sensitive = True

        i = 1
        get_next = True
        while get_next:
            get_next = False
            for file in files:
                match_a = re.search(rf"(A{i})(-(.*))*\.(png|jpg)$", file)
                if match_a is not None:
                    get_next = True
                    result.append(copy.deepcopy(template))
                    result[-1]["image1"] = os.path.join(folder_path, file)
                    if match_a.group(2) is not None:
                        result[-1]["text"] = match_a.group(3)
                    break
            if get_next:
                for file in files:
                    match_b = re.search(rf"(B{i})-(.*)\.(png|jpg)$", file, re.IGNORECASE)
                    if match_b is not None:
                        result[-1]["image2"] = os.path.join(folder_path, file)
                        tmp = rf"{self.reformat_answer(match_b.group(2))}"
                        if case_sensitive:
                            result[-1]["answer"] = re.compile(rf"^{re.escape(tmp)}$")
                        else:
                            result[-1]["answer"] = re.compile(rf"^{re.escape(tmp)}$", re.IGNORECASE)
                        break
                for file in files:
                    match_c = re.search(rf"(A{i})(-.*)*\.mp3$", file)
                    exo_question_mp3 = os.path.join(folder_path, "exo_question.mp3")
                    if os.path.isfile(exo_question_mp3):
                        result[-1]["mp3"].append(exo_question_mp3)
                        break
                    elif match_c is not None:
                        result[-1]["mp3"].append(os.path.join(folder_path, file))
                        break
            i += 1
        return result

    @staticmethod
    def get_choices(folder_path, data):
        choices_folder = os.path.join(folder_path, "choices")
        result = []
        if os.path.isdir(choices_folder):
            files = os.listdir(choices_folder)
            print(f"   ---->>choices_found")
            # Max choices is 10
            for i in range(10):
                is_found = False
                for file in files:
                    match_c = re.search(rf"(C{i + 1})(-(.*))*\.(png|jpg)$", file, re.IGNORECASE)
                    if match_c is not None:
                        # Verification
                        pass
                        result.append({"image": "", "input": "", "mp3": ""})
                        result[-1]["image"] = os.path.join(choices_folder, file)
                        if match_c.group(2):
                            result[-1]["input"] = os.path.join(choices_folder, match_c.group(2))
                        for file2 in files:
                            match_c_mp3 = re.search(rf"^(C{i}.mp3)$", file2, re.IGNORECASE)
                            if match_c_mp3 is not None:
                                result[-1]["mp3"] = os.path.join(choices_folder, file2)
                        is_found = True
                        break
                if not is_found:
                    break
        # for r in result:
        #     print(r)
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
                    data["folder_path"] = exo_path
                    try:
                        self.all_exo[exo]["exo"] = []
                        self.all_exo[exo]["min"] = int(data["min"])
                        self.all_exo[exo]["max"] = int(data["max"])
                        self.all_exo[exo]["level"] = data["level"]
                        self.all_exo[exo]["rand"] = data["rand"]
                        self.all_exo[exo]["type"] = data["type"]
                        self.all_exo[exo]["case sensitive"] = data["case sensitive"]
                        self.all_exo[exo]["comment"] = data["comment"]
                        self.all_exo[exo]["choices"] = []
                        if "library" in data:
                            self.all_exo[exo]["library"] = data["library"]
                        elif f"lib_{exo}" in sys.modules:
                            self.all_exo[exo]["library"] = f"lib_{exo}"
                        else:
                            self.all_exo[exo]["library"] = ""

                        lib = self.all_exo[exo]["library"]
                        # print(f"-->>Verification: lib = '{lib}'")
                        if lib != "" and lib in sys.modules:
                            library = sys.modules[lib]
                            for _ in range(int(data["max"])):
                                try:
                                    # TODO: avoid duplicated exo
                                    image1, image2, answer, text = library.get_image_data(data)
                                    if image1 is not None:
                                        exo_tmp = {
                                            "image1": image1,
                                            "image2": image2,
                                            "choices": [],
                                            "mp3": [],
                                            "answer": answer,
                                            "text": text
                                        }
                                        exo_question_mp3 = os.path.join(exo_path, "exo_question.mp3")
                                        if os.path.isfile(exo_question_mp3):
                                            exo_tmp["mp3"].append(exo_question_mp3)
                                        self.all_exo[exo]["exo"].append(exo_tmp)
                                except Exception as e:
                                    print(f"Exception: {e}")
                            xx = len(self.all_exo[exo]["exo"])
                            self.all_exo[exo]["min"] = min(self.all_exo[exo].get("min", float('inf')), xx)
                        # elif data["type"] == "entry":
                        else:
                            for exo_tmp in self.organize_files(exo_path, data):
                                self.all_exo[exo]["exo"].append(exo_tmp)
                            self.all_exo[exo]["choices"] = self.get_choices(exo_path, data)
                            print(f' --q-->{self.all_exo[exo]["choices"]}')
                            xx = len(self.all_exo[exo]["exo"])
                            self.all_exo[exo]["min"] = min(self.all_exo[exo].get("min", float('inf')), xx)
                    # except KeyError:
                    except Exception as e:
                        self.all_exo[exo] = {}
                        print(f"Error 12: {e}")

# p1 = ExoSchedule()
# p1.display_all_exo()
# TODO:
# - Improve entry exo
# - Crete exo from lib
# - Implement chose exo
# - Settings for schedule from UI
# - Settings for exo from UI DIALOG
# - Invent management
# - Dashboard

# EXO
#
