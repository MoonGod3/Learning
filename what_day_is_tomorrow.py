from datetime import date
from datetime import time
from datetime import datetime # this is the datetime class
import calendar


today=date.today()
days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
print("1. Tomorrow will be "+days[today.weekday()+1])


today=date.today()
days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
print("2. Tomorrow will be "+days[(today.weekday()+1)%7])