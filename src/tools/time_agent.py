import datetime

TIME_TOOL_NAME = "time_agent"
TIME_TOOL_DESCRIPTION = "Tells the user the current time of day, right now."
TIME_TOOL_PARAMETER = "none"

DATE_TOOL_NAME = "date_agent"
DATE_TOOL_DESCRIPTION = "Tells the user today's date, day, month, and year."
DATE_TOOL_PARAMETER = "none"


def get_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    return f"The current time is {now}."


def get_date():
    today = datetime.datetime.now().strftime("%d %B, %Y")
    return f"Today's date is {today}."