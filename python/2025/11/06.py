'''
Weekday finder

Given a string date in the format YYYY-MM-DD, return the day of the week.
Valid return days are:
"Sunday"
"Monday"
"Tuesday"
"Wednesday"
"Thursday"
"Friday"
"Saturday"
Be sure to ignore time zones

Test Case
1. get_weekday("2025-11-06") should return Thursday.
2. get_weekday("1999-12-31") should return Friday.
3. get_weekday("1111-11-11") should return Saturday.
4. get_weekday("2112-12-21") should return Wednesday.
5. get_weekday("2345-10-01") should return Monday.
'''

from datetime import datetime
date_string = "2025-10-31"

def get_weekday(date_string):
    # Creating an empty var for the return string
    day_of_week = ""

    # converting the string date into a datetime object
    datetime_object = datetime.strptime(date_string, "%Y-%m-%d")

    # Getting the day of the week from datetime object this is returned as an int
    datetime_object = datetime_object.weekday()

    # Converting the int value into the string day of the week
    match datetime_object:
        case 0:
            day_of_week = "Monday"
        case 1:
            day_of_week = "Tuesday"
        case 2:
            day_of_week = "Wednesday"
        case 3:
            day_of_week = "Thursday"
        case 4:
            day_of_week = "Friday"
        case 5:
            day_of_week = "Saturday"
        case 6:
            day_of_week = "Sunday"

    return day_of_week

print(get_weekday(date_string))