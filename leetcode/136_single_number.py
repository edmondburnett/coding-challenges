#!/usr/bin/env python

"""Given a non-empty array of integers, every element appears twice except for
one. Find that single one.
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] = counts[num] + 1
            else:
                counts[num] = 1
        for i in counts:
            if counts[i] == 1:
                return i


if __name__ == '__main__':
    sol = Solution()
    print(sol.singleNumber([4, , 2, 1, 2]))
    print(sol.singleNumber([7, 0, 0, 1, 7, 6, 4, 6, 4]))
    print(sol.singleNumber([3, 5, 3]))
