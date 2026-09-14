import datetime

def get_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    return f"The current time is {now}."

def get_date():
    today = datetime.datetime.now().strftime("%d %B, %Y")
    return f"Today's date is {today}."