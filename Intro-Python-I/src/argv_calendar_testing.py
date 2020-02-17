import calendar
from datetime import datetime
import sys

# print('hello')
# 1: includes only cli input and not script file at [0]
# print("This is the name of the script: ", sys.argv[1:])  # ['yo']
# print("Number of arguments: ", len(sys.argv))  # 2
# print("The arguments are: ", str(sys.argv))  # ['argv_testing.py', 'yo']


# print(datetime.now().year)  # 2020
# print(datetime.now().month)  # 2

# A Calendar object provides several methods that can be used for preparing the calendar data for formatting. This class doesn’t do any formatting itself. This is the job of subclasses.


c = calendar.TextCalendar(calendar.SUNDAY)
# formatmonth(the year, the month)
month_calendar = c.formatmonth(datetime.now().year, datetime.now().month)
# print(month_calendar)

# print(calendar.day_name[1])  # Tuesday

# Semi-Optimized
now = datetime.now()  # current local date and time e.g 2020-02-16 18:02:32.536320

# calendar.month(theyear, themonth, w=0, l=0)
# Returns a month’s calendar in a multi-line string using the formatmonth() of the TextCalendar class.

# if user provides no arguments then print calendar for current month and year
if len(sys.argv[1:]) == 0:
    # using the month function n the calendar class
    print(calendar.month(now.year, now.month))
# if the user gives 1 argument, assume month was passed in
elif len(sys.argv[1:]) == 1:
    # need to typecast to int otherwise returns a list of strings
    print(calendar.month(now.year, int(sys.argv[1])))
# if the user gives 2 arguments, assume month and year were passed in
elif len(sys.argv[1:]) == 2:
    print(calendar.month(int(sys.argv[2]), int(sys.argv[1])))
else:
    print('\n Arguments need to be given as:\n   $ 14_cal.py month [year]\n')


# Optimized

# read our arguments
args = sys.argv[1:]

year = datetime.now().year
month = datetime.now().month

if len(args) == 0:
    # if user doesn't give an input
    pass
# if the user gives 1 argument, assume month was passed in
elif len(args) == 1:
    month = int(args[0])
# if the user gives 2 arguments, assume month and year were passed in
elif len(args) == 2:
    year = int(args[1])
    month = int(args[0])
else:
    print('\n Arguments need to be given as:\n   $ 14_cal.py month [year]\n')
    exit()

print(calendar.month(year, month))
