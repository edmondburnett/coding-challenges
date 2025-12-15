#!/usr/bin/env python

# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
# https://neetcode.io/problems/duplicate-integer/question?list=blind75
# https://leetcode.com/problems/contains-duplicate/description/


class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = []
        dupe = False
        for num in nums:
            if num in seen:
                dupe = True
            seen.append(num)
        return dupe

if __name__ == "__main__":
    sol = Solution()
    print(sol.hasDuplicate([1,2,3,3]))
    print(sol.hasDuplicate([1,2,3,4]))
