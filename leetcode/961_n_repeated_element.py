#!/usr/bin/env python

"""In a array A of size 2N, there are N+1 unique elements, and exactly one of
these elements is repeated N times.

Return the element repeated N times.

In English, this problem is simply: Just return whatever number appears more
than once in the list.
"""

from typing import List


class Solution:
    def repeatedNTimes(self, A: 'List[int]') -> 'int':
        numlist = []
        for num in A:
            if num in numlist:
                return num
            else:
                numlist.append(num)


if __name__ == '__main__':
    sol = Solution()
    print(sol.repeatedNTimes([5,1,5,2,5,3,5,4]))
