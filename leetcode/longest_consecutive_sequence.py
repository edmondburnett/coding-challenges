#!/usr/bin/env python

# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. 
# The elements do not have to be consecutive in the original array.

# https://neetcode.io/problems/longest-consecutive-sequence/question?list=blind75

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        nums_sorted = sorted(set(nums))
        max_length = 1
        current_length = 1

        for i in range(len(nums_sorted) -1):
            if nums_sorted[i+1] - nums_sorted[i] == 1:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 1

        # Check the final sequence
        max_length = max(max_length, current_length)
        return max_length



class Solution2:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)
        max_length = 0
        
        for num in num_set:
            # Only start counting if this is the beginning of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                
                # Count consecutive numbers
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                max_length = max(max_length, current_length)
        
        return max_length


if __name__ == "__main__":
    sol = Solution()
    sol2 = Solution2()

    print(sol.longestConsecutive([2,20,4,10,3,4,5]))  # 4
    print(sol2.longestConsecutive([2,20,4,10,3,4,5]))  # 4
    print(sol.longestConsecutive([0,3,2,5,4,6,1,1]))  # 7
    print(sol2.longestConsecutive([0,3,2,5,4,6,1,1]))  # 7
