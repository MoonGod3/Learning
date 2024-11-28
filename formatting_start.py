#
# Example file for formatting time and date output
# LinkedIn Learning Python course by Joe Marini
#


from datetime import datetime

def main():
    # Times and dates can be formatted using a set of predefined string
    # control codes 

    
    #### Date Formatting ####
    
    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    now = datetime.now()
    # print(now.strftime("The current year is: %Y")) #%Y for 4 digit year
    # print(now.strftime("The current year is: %y")) #%y for 2 digit year
    # print(now.strftime("The current month is: %B")) #%B for Full name of month
    # print(now.strftime("The current month is: %b")) #%b for 3 ltr month
    # print(now.strftime("The current date is: %D")) #%D for full date in mm/dd/yy
    # print(now.strftime("The current date is: %d")) #%d for just the two digit date
    # print(now.strftime("The current day is: %A")) #%A for full name of day
    # print(now.strftime("The current day is: %a")) #%a for 3 ltr name of day

    # print(now.strftime("The current year is: %Y"))
    # print(now.strftime("%a, %d %B, %Y"))

    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print(now.strftime("Locale date and time: %c"))    
    print(now.strftime("Locale date: %x"))    
    print(now.strftime("Locale time: %X"))    



    #### Time Formatting ####
    
    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print(now.strftime("Current time: %I:%M:%S %p")) #%I for 0-12 hr, %M min, %S seconds, %p for AM/PM
    print(now.strftime("24-hour time: %H:%M:%S")) #%H for 0-24 hr Military Time
    print(now.strftime("24-hour time: %H:%M:%S")+" Hours") #%H for 0-24 hr Military Time

if __name__ == "__main__":
    main()
