import datetime

def current_date():
    current_date = datetime.datetime.now().strftime("%d/%m/%Y")
    return current_date

def current_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return current_time

def date_time():
    current_date_time = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    return current_date_time
