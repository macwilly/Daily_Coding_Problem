'''
Is it the weekend?

Given a date in the format "YYYY-MM-DD", return the number of days left until the weekend.

 * The weekend starts on Saturday.
 * If the given date is Saturday or Sunday, return "It's the weekend!".
 * Otherwise, return "X days until the weekend.", where X is the number of days until Saturday.
 * If X is 1, use "day" (singular) instead of "days" (plural).
 * Make sure the calculation ignores your local timezone.

Test Case
1. days_until_weekend("2025-11-14") should return "1 day until the weekend."
2. days_until_weekend("2025-01-01") should return "3 days until the weekend."
3. days_until_weekend("2025-12-06") should return "It's the weekend!"
4. days_until_weekend("2026-01-27") should return "4 days until the weekend."
5. days_until_weekend("2026-09-07") should return "5 days until the weekend."
6. days_until_weekend("2026-11-29") should return "It's the weekend!"

-NOTE-
Reused some code from 11/06/2025
'''

from datetime import datetime

def days_until_weekend(date_string):

    # converting the string date into a datetime object
    datetime_object = datetime.strptime(date_string, "%Y-%m-%d")

    # Getting the day of the week from datetime object this is returned as an int
    datetime_object = datetime_object.weekday()

    # If it is Saturday or Sunday do not do calculation and just return "It's the weekend!"
    if datetime_object == 5 or datetime_object == 6:
        return "It's the weekend!"
    else:
        # Calculate day(s) until the weekend, hard coding 5 as that is the default int for saturday in python
        days_difference = 5 - datetime_object
        if days_difference > 1:
            return f"{days_difference} days until the weekend."
        else:
            return "1 day until the weekend."


test_arr = [
    "2025-11-14",
    "2025-01-01",
    "2025-12-06",
    "2026-01-27",
    "2026-09-07",
    "2026-11-29",
]

for date_string in test_arr:
    print(days_until_weekend(date_string))