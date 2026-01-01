#!/usr/bin/env python

# https://leetcode.com/problems/3sum/description/
# https://neetcode.io/problems/three-integer-sum/question

# Algorithm type: Two-Pointer


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []
        nums.sort()

        for index, a in enumerate(nums):
            if index > 0 and a == nums[index - 1]:
                continue

            left = index + 1
            right = len(nums) - 1

            while left < right:
                three_sum = a + nums[left] + nums[right]
                if three_sum > 0:
                    right = right - 1
                elif three_sum < 0:
                    left = left + 1
                else:
                    result.append([a, nums[left], nums[right]])
                    left = left + 1
                    right = right - 1
                    while left < right and nums[left] == nums[left - 1]:
                        left = left + 1
                    while right > left and nums[right] == nums[right + 1]:
                        right = right - 1
        return result


sol = Solution()

assert sol.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
assert sol.threeSum([0, 1, 1]) == []
assert sol.threeSum([0, 0, 0, 0]) == [[0, 0, 0]]
assert sol.threeSum([-2, 0, 0, 2, 2]) == [[-2, 0, 2]]

print("All tests passed!")
