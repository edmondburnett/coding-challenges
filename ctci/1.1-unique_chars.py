#!/usr/bin/env python

"""Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?

Page 90, 1.1

Other possible variations: No use of Python "in"; recursive; sort then divide
and conquer; using a list of bools.
"""


def unique_chars(string: str) -> bool:
    if len(string) > 256:
        # Assuming extended ASCII, a len > 256 would indicate presence of non-unique chars
        return False

    result = False
    for i in range(len(string)):
        if string[i] not in string[i + 1:]:
            result = True
        else:
            return False
    return result


if __name__ == "__main__":
    print(unique_chars("hello"))
    print(unique_chars("fubar"))
    print(unique_chars("abcdefghHijklmnopqrstuvwxyzABC"))
