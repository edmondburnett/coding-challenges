#!/usr/bin/env python

"""Given a List of words, return the words that can be typed using letters of
alphabet on only one row's of American keyboard like the image below.
"""

from typing import List


class Solution:
    def __init__(self):
        self.row1 = "qwertyuiopQWERTYUIOP"
        self.row2 = "asdfghjklASDFGHJKL"
        self.row3 = "zxcvbnmZXCVBNM"

    def findWords(self, words: List[str]) -> List[str]:
        one_row_words = []
        for word in words:
            r1 = 0
            r2 = 0
            r3 = 0
            for letter in word:
                if letter in self.row1:
                    r1 += 1
                elif letter in self.row2:
                    r2 += 1
                elif letter in self.row3:
                    r3 += 1
            print(word, r1, r2, r3)
            if len(word) == r1 or len(word) == r2 or len(word) == r3:
                one_row_words.append(word)
        return one_row_words


if __name__ == '__main__':
    sol = Solution()
    print(sol.findWords(["Hello", "Alaska", "Dad", "Peace", "hello"]))
    print(sol.findWords(["adsdf", "sfd", "glass"]))
