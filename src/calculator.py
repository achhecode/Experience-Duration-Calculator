import json
from models import DateRange, Experience

class ExperienceCalculator:
    def __init__(self, json_path: str):
        self.json_path = json_path

    def load_experience(self):
        with open(self.json_path, "r") as file:
            return json.load(file)

    def calculate_total_experience(self):
        data = self.load_experience()
        total_months = 0

        for entry in data.values():
            date_range = DateRange(
                entry["from"]["month"],
                entry["from"]["year"],
                entry["to"]["month"],
                entry["to"]["year"]
            )
            experience = Experience(date_range)
            total_months += experience.get_months()

        years = total_months // 12
        months = total_months % 12
        return years, months
