#!/usr/bin/env python

# Design an algorithm to encode a list of strings to a single string. 
# The encoded string is then decoded back to the original list of strings.
# https://neetcode.io/problems/string-encode-and-decode/question?list=blind75
# https://leetcode.com/problems/encode-and-decode-strings/description/


class Solution:
    def encode(self, strs: list[str]) -> str:
        return "#".join(strs)

    def decode(self, s: str) -> list[str]:
        return s.split("#")
