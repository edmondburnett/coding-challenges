#!/usr/bin/env python

# page 73, problem 1.1
# Implement an algorithm to determine if a string has all unique characters.
# bonus: use no other data structures

import sys


# try also an alternate version which uses recursion and possibly an optional argument
def unique_chars(string):
    cur_char = ""
    for letter in string:
        if letter not in cur_char:
            cur_char = cur_char + letter
            result = True
        else:
            result = False
            break
    return result


if __name__ == '__main__':
    try:
        input_string = sys.argv[1]
    except IndexError:
        print("No input string supplied.")
        sys.exit()

    print(f"Are all characters of {input_string} unique? {unique_chars(input_string)}")
