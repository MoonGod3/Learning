from datetime import date
from datetime import time
from datetime import datetime # this is the datetime class
import calendar

show_expected_result = True
show_hints = True

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] ##This list is used below!


def count_days(year, month, whichday):
    # Your code goes here.
    desired_day = days[whichday]
    
    # need to know how many days in "month" for a given "year"
    days_in_month = calendar.monthrange(year, month)

    cnt = 0
    for i in range(1, int(days_in_month[1]) + 1):
        # Creating a date object
        date_object = datetime(year, month, i)
        # Getting the day name
        day_name = date_object.strftime("%A")

        if day_name == desired_day:
            cnt += 1
        # print("This date corresponds  to:", day_name)
    #print("There are ", cnt, desired_day, "s in this year month #combo")

    return cnt