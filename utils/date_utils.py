import calendar
from datetime import date


def is_today_the_last_day_in_current_month():
    today = date.today().strftime("%Y-%m-%d")
    current_year = int(today[:4])
    current_month = int(today[5:7])
    current_day = int(today[8:])
    if calendar.monthrange(current_year, current_month)[1] == current_day:
        return True
    else:
        return False
