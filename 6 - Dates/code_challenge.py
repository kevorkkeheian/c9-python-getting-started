

# print the date one week from the date entered

from datetime import datetime  #To extract date and time functions
from datetime import timedelta #To extract functions such as timedelta

today = datetime.now()


# print today's date
print(today)

# print yesterday's date
one_day = timedelta(days = 1)
yesterday = today - one_day
print("yesterday was " + str(yesterday))


# ask a user to enter a date
birthday = input("Please enter your birthday (dd/mm/yyyy): ")
birthday_day = datetime.strptime(birthday, '%d/%m/%Y')
print("Birhtday: " + str(birthday_day))

# print the date one week from the date entered
seven_days = timedelta(days = 7)
print(birthday_day - seven_days)