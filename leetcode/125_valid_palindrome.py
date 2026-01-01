#!/usr/bin/env python

# https://neetcode.io/problems/is-palindrome/question?list=blind75
# https://leetcode.com/problems/valid-palindrome/description/

import re



class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Reverse and compare solution"""
        rev = s[::-1].lower().replace(" ", "")
        rev = re.sub(r'[^a-zA-Z0-9]', '', rev)
        if rev[::-1] == rev:
            return True
        return False

    def isPalindrome2(self, s: str) -> bool:
        """Two-Pointer solution"""
        left = 0
        right = len(s) - 1

        while left < right:
            # skip non-alphanumeric chars from each direction
            while left < right and not s[left].isalnum():
                left = left + 1
            while left < right and not s[right].isalnum():
                right = right - 1

            # don't allow the pointers to cross
            if left >= right:
                break

            if s[left].lower() != s[right].lower():
                return False

            left = left + 1
            right = right - 1

        return True

if __name__ == '__main__':
    sol = Solution()
    assert sol.isPalindrome("Was it a car or a cat I saw?") == True
    assert sol.isPalindrome("tab a cat") == False
    
    assert sol.isPalindrome2("Was it a car or a cat I saw?") == True
    assert sol.isPalindrome2("tab a cat") == False
    assert sol.isPalindrome2("") == True
    assert sol.isPalindrome2("a") == True
    assert sol.isPalindrome2("A man, a plan, a canal: Panama") == True
    assert sol.isPalindrome2("race a car") == False
    assert sol.isPalindrome2("a,,a") == True

    print("All test cases passed!")

