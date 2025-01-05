import json
import random
import lib_addition_3ch_hor
from datetime import date
import os


class ExoSchedule:
    def __init__(self):
        self.exo_dir = r"C:\Users\NJAKA\Desktop\exo_itk"
        self.exo_schedule = "exo_schedule.json"
        self.all_exo = {}
        self.load_all_exo()
        self.update_all_exo()

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
                    random_values = random.sample(schedule['exo_group'], schedule['exo_number'])
                    for exo in random_values:
                        self.all_exo[exo] = {}

        # print(self.all_exo)
        # print(f"Today is: {self.get_today_weekday()}")

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

                        if exo == "addition_3ch_hor":
                            for _ in range(int(data["max"])):
                                image1, image2, answer = lib_addition_3ch_hor.get_image(1)
                                exo_tmp = {
                                    "image1": image1,
                                    "image2": image2,
                                    # "image1": "images/A1.png",
                                    # "image2": "images/A4.png",
                                    "mp3": None,
                                    "answer": answer,
                                    "text": "andrana"
                                }
                                self.all_exo[exo]["exo"].append(exo_tmp)
                    except KeyError:
                        self.all_exo[exo] = {}
                        print("Error 12")

                # print(json_config_path)


# p1 = ExoSchedule()
# p1.display_all_exo()
