#!/usr/bin/env python

# https://neetcode.io/problems/is-palindrome/question?list=blind75
# https://leetcode.com/problems/valid-palindrome/description/

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return false

        rev = s[::-1].lower().replace(" ", "")
        rev = re.sub(r'[^a-zA-Z0-9]', '', rev)
        if rev[::-1] == rev:
            return True
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindrome("Was it a car or a cat I saw?"))  # True
    print(sol.isPalindrome("tab a cat"))  # False
