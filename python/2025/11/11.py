'''
Vowels and Consonants

Given a string, return an array with the number of vowels and number of consonants in the string.
 * Vowels consist of a, e, i, o, u in any case.
 * Consonants consist of all other letters in any case.
 * Ignore any non-letter characters.

Test Case
1.  count("Hello World") should return [3, 7].
2. count("JavaScript") should return [3, 7].
3. count("Python") should return [1, 5].
4. count("freeCodeCamp") should return [5, 7].
5. count("Hello, World!") should return [3, 7].
6. count("The quick brown fox jumps over the lazy dog.") should return [11, 24].
'''

def count(s):
    # Initialize the return count
    count = []
    # Initialize the counts
    vowel_count = 0
    consonant_count = 0

    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q',
                  'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    # setting the giving string to lower to ignore case.
    s = s.lower()
    for char in s:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1

    count.append(vowel_count)
    count.append(consonant_count)

    return count

test_arr = [
    "Hello World",
    "JavaScript",
    "Python",
    "freeCodeCamp",
    "Hello, World!",
    "The quick brown fox jumps over the lazy dog."
]

for filename in test_arr:
    print(count(filename))