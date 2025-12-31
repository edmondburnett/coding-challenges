#!/usr/bin/env python

# https://leetcode.com/problems/container-with-most-water/description/
# https://neetcode.io/problems/max-water-container/question

# Algorithm type: Two-Pointer


class Solution:
    @classmethod
    def maxArea(self, heights: list[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            height = min(heights[left], heights[right])
            width = right - left

            area = height * width
            if area > max_area:
                max_area = area

            if heights[left] < heights[right]:
                left = left + 1
            else:
                right = right - 1
        
        return max_area


if __name__ == "__main__":
    assert Solution.maxArea([1,7,2,5,4,7,3,6]) == 36
    assert Solution.maxArea([2,2,2]) == 4
    assert Solution.maxArea([1,8,6,2,5,4,8,3,7]) == 49
