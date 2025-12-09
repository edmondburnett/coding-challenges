#!/usr/bin/env python

# https://neetcode.io/problems/is-palindrome/question?list=blind75
# https://leetcode.com/problems/valid-palindrome/description/

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev = ''.join(reversed(s)).lower().replace(" ", "")
        rev = re.sub(r'[^a-zA-Z0-9\s]', '', rev)
        if ''.join(reversed(rev)) == rev:
            return True
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindrome("Was it a car or a cat I saw?"))
    print(sol.isPalindrome("tab a cat"))
