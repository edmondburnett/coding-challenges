#!/usr/bin/env python

import string
from typing import List

morse_codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
alphabet = string.ascii_lowercase  # problem specifies lowercase-only input


class Solution:
    def __init__(self):
        self.morse_dict = self.create_dict(alphabet, morse_codes)

    def create_dict(self, alphabet: 'str', morse_codes: 'List[str]') -> 'dict':
        dictionary = {}
        for i in range(len(alphabet)):
            dictionary[alphabet[i]] = morse_codes[i]
        return dictionary

    def uniqueMorseRepresentations(self, words: 'List[str]') -> 'int':
        morse_set = set()
        for word in words:
            morse_word = ""
            for letter in word:
                morse_word = morse_word + self.morse_dict[letter]
            morse_set.add(morse_word)
        return len(morse_set)


if __name__ == '__main__':
    sol = Solution()
    result = sol.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
    print(result)
