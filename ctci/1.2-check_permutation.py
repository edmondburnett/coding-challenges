#!/usr/bin/env python

"""Given two strings, write a method to decide if one is a permutation of
the other.

Page 90, 1.2

Possible variations: Sort both strings first
"""


def permutation(A: str, B: str) -> bool:
    """ An easy Python way. Sort both strings and compare.
        Should be O(n log n) worst case, sorted() uses Timsort.
    """
    a = ''.join(sorted(A))
    b = ''.join(sorted(B))
    if a in b:
        return True
    return False


if __name__ == "__main__":
    print(permutation("god", "dog"))
    print(permutation("god", "analog"))
