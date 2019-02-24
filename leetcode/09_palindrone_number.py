#!/usr/bin/env python


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        r = "".join(reversed(str(x)))
        if s == r:
            return True
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindrome(10))
