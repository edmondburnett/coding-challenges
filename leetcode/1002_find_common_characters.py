#!/usr/bin/env python

"""Given an array A of strings made only from lowercase letters, return a list
of all characters that show up in all strings within the list (including
duplicates).  For example, if a character occurs 3 times in all strings but not
4 times, you need to include that character three times in the final answer.

You may return the answer in any order.
"""

from typing import List
from functools import reduce
from collections import Counter


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        result = reduce(lambda x, y: x & y, map(lambda x: Counter(x), A))
        return list(result.elements())


if __name__ == "__main__":
    l1 = ["bella", "label", "roller"]
    l2 = ["cool", "lock", "cook"]
    s = Solution()
    print(s.commonChars(l1))
    print(s.commonChars(l2))
