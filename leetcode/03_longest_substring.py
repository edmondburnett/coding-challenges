#!/usr/bin/env python

# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# https://neetcode.io/problems/longest-substring-without-duplicates/question?list=blind75

# Algorithm type: Sliding Window


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set: set[str] = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            # if duplicate, shrink window from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])

            max_length = max(max_length, right - left + 1)

        return max_length


sol = Solution()
assert sol.lengthOfLongestSubstring("abcabcbb") == 3
assert sol.lengthOfLongestSubstring("pwwkew") == 3
assert sol.lengthOfLongestSubstring("abba") == 2
assert sol.lengthOfLongestSubstring("bbbbb") == 1

print("All tests passed!")
