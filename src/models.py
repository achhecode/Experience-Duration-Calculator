from datetime import datetime

class DateRange:
    def __init__(self, start_month, start_year, end_month, end_year):
        self.start = datetime.strptime(f"{start_month} {start_year}", "%B %Y")
        self.end = datetime.strptime(f"{end_month} {end_year}", "%B %Y")

    def duration_in_months(self) -> int:
        return (self.end.year - self.start.year) * 12 + (self.end.month - self.start.month)


class Experience:
    def __init__(self, date_range: DateRange):
        self.date_range = date_range

    def get_months(self) -> int:
        return self.date_range.duration_in_months()
