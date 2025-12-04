#!/usr/bin/env python

# https://leetcode.com/problems/valid-anagram/
# https://neetcode.io/problems/is-anagram/question?list=blind75

class Solution:
    @classmethod
    def isAnagram(cls, s: str, t: str) -> bool:
        a = sorted(s)
        b = sorted(t)
        if a == b:
            return True
        return False


if __name__ == '__main__':
    print(Solution.isAnagram("racecar", "carrace"))
    print(Solution.isAnagram("jar", "jam"))
