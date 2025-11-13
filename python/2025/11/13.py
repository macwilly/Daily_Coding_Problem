'''
Array Shift

Given an array and an integer representing how many positions to shift the array, return the shifted array.

 * A positive integer shifts the array to the left.
 * A negative integer shifts the array to the right.
 * The shift wraps around the array.
For example, given [1, 2, 3] and 1, shift the array 1 to the left, returning [2, 3, 1].

Test Case
1. shift_array([1, 2, 3], 1) should return [2, 3, 1].
2. shift_array([1, 2, 3], -1) should return [3, 1, 2].
3. shift_array(["alpha", "bravo", "charlie"], 5) should return ["charlie", "alpha", "bravo"].
4. shift_array(["alpha", "bravo", "charlie"], -11) should return ["bravo", "charlie", "alpha"]
5. shift_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 15) should return [5, 6, 7, 8, 9, 0, 1, 2, 3, 4].
'''

def shift_array(arr, n):
    # Initialize return array
    return_array = []
    # Getting the array length once to use multiple times
    array_length = len(arr)
    # Using enumerate to be able to get the index of the array to be able to manipulate it
    for index, item in enumerate(arr):
        # New index is calculated by subtracting the shift argument from the original index to move it left or right then doing mod of the array length to get correct index
        new_index = (index - n) % array_length
        # inserting to the return array to set the appropriate index
        return_array.insert(new_index, item)

    return return_array

test_arr = [
    {"Array":[1,2,3], "Shift": 1},
    {"Array":[1,2,3], "Shift": -1},
    {"Array":["alpha", "bravo", "charlie"], "Shift": 5},
    {"Array":["alpha", "bravo", "charlie"], "Shift": -11},
    {"Array":[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], "Shift": 15}
]

for arr in test_arr:
    print(shift_array(arr["Array"], arr["Shift"]))