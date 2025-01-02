import json
import random
import lib_addition_3ch_hor
from datetime import date, timedelta
import os


class ExoSchedule:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.exo_dir = r"C:\Users\NJAKA\Desktop\exo_itk"
        self.exo_schedule = "exo_schedule.json"
        self.all_exo = {}

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
                    # print(data)
                    # TODO: Need to check the data if correct
                    self.all_exo[exo] = data
                # print(json_config_path)


p1 = ExoSchedule("John", 36)
p1.load_all_exo()
p1.update_all_exo()
p1.display_all_exo()
