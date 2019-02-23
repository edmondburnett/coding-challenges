#!/usr/bin/env python

"""Given two strings A and B, find the minimum number of times A has to be
repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring
of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
"""


class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        repeat_count = 0
        repeated = ''
        while len(repeated) <= 10000:
            if B in repeated:
                return repeat_count
            else:
                repeated = repeated + A
                repeat_count += 1
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.repeatedStringMatch("abcd", "cdabcdab"))  # 3
    print('------')
    print(sol.repeatedStringMatch("abc", "cabcabca"))  # 4
