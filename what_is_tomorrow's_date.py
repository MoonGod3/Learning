from datetime import date
from datetime import time
from datetime import datetime # this is the datetime class
import calendar
from datetime import timedelta

today = date.today()

# Option A:
tomorrow1 = today+timedelta(days=1)
# Option B:
tomorrow2 = date(today.year,today.month,today.day+1)

print(tomorrow1, tomorrow2)