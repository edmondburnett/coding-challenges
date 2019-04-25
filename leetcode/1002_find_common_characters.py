#!/usr/bin/env python

"""Given an array A of strings made only from lowercase letters, return a list
of all characters that show up in all strings within the list (including
duplicates).  For example, if a character occurs 3 times in all strings but not
4 times, you need to include that character three times in the final answer.

You may return the answer in any order.
"""

from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        charlist = []
        for word in A:
            for letter in word:
                charlist.append(letter)
        final_list = charlist.copy()
        for char in charlist:
            for word in A:
                final_list = list(filter(lambda x: x in word, final_list))
        return final_list


if __name__ == "__main__":
    l1 = ["bella", "label", "roller"]
    l2 = ["cool", "lock", "cook"]
    s = Solution()
    print(s.commonChars(l1))
