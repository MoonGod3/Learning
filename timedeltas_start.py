#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# TODO: construct a basic timedelta and print it
# print(timedelta(days=365, hours=5, minutes=1))

# TODO: print today's date
now = datetime.now()
# print("Today is", now)


# TODO: print today's date one year from now
# print("One year from now will be", str(now + timedelta(days = 365)))

# TODO: create a timedelta that uses more than one argument
# print("In two weeks and 3 days, it will be", str(now + timedelta(days=14, hours=71, minutes=60)))
# print("In two weeks and 3 days, it will be", str(now + timedelta(weeks=2, days=3)))

# TODO: calculate the date 1 week ago, formatted as a string
# t = datetime.now() - timedelta(weeks=1)
# s = t.strftime("%A %B %d, %Y")
# print("A week ago, it was", str(now + timedelta(weeks=-1))) ##Not in string format!
# print("A week ago, it was", s) ## In string format!!

### How many days until April Fools' Day?
today = date.today()
print(today, end="\n\n")
afd = date(today.year, 4, 1)
#print(afd)

# TODO: use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
    print("Shucks, April Fool's day has already come and gone this year.", end="\n\n")
    afd = afd.replace(year = today.year + 1)
    #afd = date(today.year, 4, 1) + timedelta(days = 365)

# TODO: Now calculate the amount of time until April Fool's Day  
time_to_afd = afd - today
# print(time_to_afd)
# print(time_to_afd.days)
print("There are", time_to_afd.days, " days till next April Fool's Day")
