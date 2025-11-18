'''
100 Characters

Welcome to the 100th Daily Coding Challenge!

Given a string, repeat its characters until the result is exactly 100 characters long. If your repetitions go over
100 characters, trim the extra so it's exactly 100.



Test Case
1. oneHundred("One hundred ") should return
   "One hundred One hundred One hundred One hundred One hundred One hundred One hundred One hundred One ".
2. oneHundred("freeCodeCamp ") should return
   "freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeC".
3. oneHundred("daily challenges ") should return
   "daily challenges daily challenges daily challenges daily challenges daily challenges daily challenge".
4. oneHundred("!") should return
   "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!".
'''

def one_hundred(chars):
    # Creating a return string
    return_string = ""
    # Quickly running the loop 100 times. This could also be done with a while loop to reduce number of calls
    # memory size. The while loop is probably the better idea.
    # for i in range(0,101):
    #     return_string += chars
    while len(return_string) <= 100:
        return_string += chars

    # Checking if the length is greater than 100
    if(len(return_string) > 100):
        # returning the first 100 characters
        return_string = return_string[0:100]

    return return_string

test_arr = [
    "One hundred ",
    "freeCodeCamp ",
    "daily challenges ",
    "!",
]

for test_string in test_arr:
    print(one_hundred(test_string))
    print(len(one_hundred(test_string)))