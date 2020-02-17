"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`

and does the following:
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to
print out a calendar for April in 2015, but if you omit either the year or both values,
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

#  - If the user doesn't specify any input, your program should
#    print the calendar for the current month. The 'datetime'
#    module may be helpful for this.

# '1:' includes only cli input and not script file at [0]
user_input = sys.argv[1:]
c = calendar.TextCalendar(calendar.SUNDAY)

# datetime.now() = current local date and time e.g 2020-02-16 18:02:32.536320

# if user doesn't give an input
if len(user_input) == 0:
    # print calendar for current month
    month_calendar = c.formatmonth(datetime.now().year, datetime.now().month)
    print(month_calendar)
    # if the user gives one argument
elif len(user_input) == 1:
    # assume month was passed in and render calendar for that month of the current year
    month_calendar = c.formatmonth(datetime.now().year, int(user_input[0]))
    print(month_calendar)
# if the user gives two arguments
elif (len(user_input) == 2):
    # assume month and year was passed in and render calendar for that month and year
    month_calendar = c.formatmonth(int(user_input[1]), int(user_input[0]))
    print(month_calendar)
else:
    # print format that arguments need to be given and then exit the program
    print(
        "arguments need to be given as [month] [year] with year being optional, in this format: 'python 14_cal.py 3 2001")

# Optimized Version -------- Run in argv_calendar_testing.py

# SIMPLIFYING
now = datetime.now()  # current local date and time e.g 2020-02-16 18:02:32.536320

# calendar.month(theyear, themonth, w=0, l=0)
# Returns a month’s calendar in a multi-line string using the formatmonth() of the TextCalendar class.

# if user provides no arguments then print calendar for current month and year
if len(sys.argv[1:]) == 0:
    # using the month function n the calendar class
    print(calendar.month(now.year, now.month))
# if the user gives 1 argument, assume month was passed in
elif len(sys.argv[1:]) == 1:
    print(calendar.month(now.year, int(sys.argv[1])))
# if the user gives 2 arguments, assume month and year were passed in
elif len(sys.argv[1:]) == 2:
    print(calendar.month(int(sys.argv[2]), int(sys.argv[1])))
else:
    print('\n Arguments need to be given as:\n   $ 14_cal.py month [year]\n')
