'''
Character Count

Given a sentence string, return an array with a count of each character in alphabetical order.

 * Treat upper and lowercase letters as the same letter when counting.
 * Ignore numbers, spaces, punctuation, etc.
 * Return the count and letter in the format "letter count". For instance, "a 3".
 * All returned letters should be lowercase.
 * Do not return a count of letters that are not in the given string.

Test Case
1. count_characters("hello world")
    should return ["d 1", "e 1", "h 1", "l 3", "o 2", "r 1", "w 1"].
2. count_characters("I love coding challenges!")
    should return ["a 1", "c 2", "d 1", "e 3", "g 2", "h 1", "i 2", "l 3", "n 2", "o 2", "s 1", "v 1"].
3. count_characters("// TODO: Complete this challenge ASAP!")
    should return ["a 3", "c 2", "d 1", "e 4", "g 1", "h 2", "i 1", "l 3", "m 1", "n 1", "o 3", "p 2", "s 2", "t 3"].
'''

def count_characters(sentence):
    # Setting up dictionary
    count_dict = {}
    # setting up return array
    ret_array = []
    # String to lower to ignore case and return as lower case
    sentence = sentence.lower()


    for char in sentence:
        # Only counting the alphabetic characters
        if char.isalpha():
            # Adding the character to the dictionary with character as key and count as value
            count_dict.update({char:sentence.count(char)})
    # Sorting the dictionary
    sorted_item = sorted(count_dict.items())

    # creating the string format for the return and adding to the return array
    for key,value in sorted_item:
        ret_array.append(f"{key} {value}")

    return ret_array




test_arr = [
    "hello world",
    "I love coding challenges!",
    "// TODO: Complete this challenge ASAP!"
]

for test_string in test_arr:
    print(count_characters(test_string))
