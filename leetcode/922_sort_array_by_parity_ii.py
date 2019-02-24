#!/usr/bin/env python

"""Given an array A of non-negative integers, half of the integers in A are
odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is
even, i is even.

You may return any answer array that satisfies this condition.
"""

from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        newlist = [None] * len(A)

        index = 0
        for num in A:
            if num % 2 == 0:
                newlist[index] = num
                index += 2

        index = 1
        for num in A:
            if num % 2 == 1:
                newlist[index] = num
                index += 2

        return newlist



if __name__ == '__main__':
    sol = Solution()
    print(sol.sortArrayByParityII([4, 2, 5, 7]))
    print(sol.sortArrayByParityII([5, 7, 1, 6, 8, 2]))
