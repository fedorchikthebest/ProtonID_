import datetime


def current_jule():
    current_time = datetime.date(datetime.datetime.now().year, datetime.datetime.now().month, day=1)
    if current_time.month < 6:
        current_time = datetime.date(current_time.year - 1, 6, 1)
    return current_time