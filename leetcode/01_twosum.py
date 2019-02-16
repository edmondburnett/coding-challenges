#!/usr/bin/env python

"""Two Sum

Given an array of integers, return indices of the two numbers such that they
add up to a specific target. You may assume that each input would have exactly
one solution, and you may not use the same element twice.
"""

from typing import List, Optional
from time import perf_counter
import itertools as it


class Solution:
    def TwoSum(self, nums: List[int], target: int) -> Optional[List[int]]:
        """ First attempt, for loop brute force """
        for i in range(len(nums)):
            for x in range(len(nums)):
                if i == x:
                    continue
                if nums[i] + nums[x] == target:
                    return [i, x]
        return None

    def TwoSum2(self, nums: List[int], target: int) -> Optional[List[int]]:
        """ using itertools """
        length = len(nums)
        for i, x, in it.combinations(range(length), r=2):
            if nums[i] + nums[x] == target:
                return [i, x]
        return None


if __name__ == '__main__':
    list1 = [2, 7, 11, 15]  # 9
    list2 = [13, 1, 7, 2, 6]  # 13
    list3 = [3, 2, 4]  # 6
    list4 = [3, 0, 4, 9, 12]  # 4

    sol = Solution()
    start = perf_counter()
    #print(sol.TwoSum(list4, 4))
    print(sol.TwoSum2(list3, 6))
    end = perf_counter()
    print(end - start)
