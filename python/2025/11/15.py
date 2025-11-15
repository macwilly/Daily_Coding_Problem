'''
GCD
Given two positive integers, return their greatest common divisor (GCD).

 * The GCD of two integers is the largest number that divides evenly into both numbers without leaving a remainder.

For example, the divisors of 4 are 1, 2, and 4. The divisors of 6 are 1, 2, 3, and 6.
So given 4 and 6, return 2, the largest number that appears in both sets of divisors.

Test Case
1. gcd(4, 6) should return 2.
2. gcd(20, 15) should return 5.
3. gcd(13, 17) should return 1.
4. gcd(654, 456) should return 6.
5. gcd(3456, 4320) should return 864.


'''

def gcd(int_a, int_b):

    # setting the lager and smaller ints so that the function is agnostic of which order the arguments are in
    if int_a > int_b:
        larger = int_a
        smaller = int_b
    else:
        larger = int_b
        smaller = int_a

    # Using the Euclidean Algorithm. Also thought about doing the list method
    while smaller != 0:
        mod = larger % smaller
        if mod == 0:
            return smaller
        else:
            larger = smaller
            smaller = mod

    return smaller

test_arr = [
    [4,6],
    [20,15],
    [13,17],
    [654,456],
    [3456,4320]
]

for test_ints in test_arr:
    print(gcd(test_ints[0], test_ints[1]))