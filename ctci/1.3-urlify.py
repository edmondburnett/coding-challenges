#!/usr/bin/env python

"""Write a method to replace all spaces in a string with %20.
You may assume that the string has sufficient space to hold the additional
characters, and that you are given the 'true' length of the string.

Example:
Input:  'Mr John Smith    ', 13
Output: 'Mr%20John%20Smith'

Soltion ideas:
- Use Regex to find the spaces bordered by other chars, then count and replace
those, truncating the ending spaces by the count.
- for loop through the string backwards and count the spaces at the end ...
"""


def count_spaces(string: str, length: int, target) -> int:
    count = 0
    for i in range(length):
        if string[i] == target:
            count += 1
    return count


def urlify(string: str, truelength: int) -> str:
    num_spaces = count_spaces(string, truelength, ' ')
    new_index = truelength - 1 + num_spaces * 2
    string_list = list(string)

    for old_index in reversed(range(truelength)):
        if string_list[old_index] == ' ':
            string_list[new_index] = '0'
            string_list[new_index - 1] = '2'
            string_list[new_index - 2] = '%'
            new_index -= 3
        else:
            string_list[new_index] = string_list[old_index]
            new_index -= 1

    return ''.join(string_list)



if __name__ == "__main__":
    print(urlify('Mr John Smith    ', 13))
    print(urlify('Silly Bean Edmond Dantes      ', 24))
