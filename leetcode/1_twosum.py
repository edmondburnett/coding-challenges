#!/usr/bin/env python

# https://leetcode.com/problems/two-sum/
# https://neetcode.io/problems/two-integer-sum/question?list=blind75

class Solution:
    @classmethod
    def twoSum(cls, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            other = target - num
            if other in seen:
                return [seen[other], i]
            seen[num] = i


if __name__ == '__main__':
    print(Solution.twoSum([3,4,5,6], 7))
    print(Solution.twoSum([4,5,6], 10))
