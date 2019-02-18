#!/usr/bin/env python

"""Given an array A of non-negative integers, return an array consisting of all
the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.
"""

from typing import List


class Solution:
    def sortArrayByParity(self, A: 'List[int]') -> 'List[int]':
        parity = []
        for n in A:
            if n % 2 == 0:
                parity.append(n)
        for x in A:
            if x % 2 != 0:
                parity.append(x)
        return parity


if __name__ == '__main__':
    sol = Solution()
    print(sol.sortArrayByParity([3, 1, 2, 4, 7, 2, 8, 10, 500, 999]))
