#!/usr/bin/env python

# https://leetcode.com/problems/group-anagrams/
# https://neetcode.io/problems/anagram-groups/question?list=blind75

from typing import List

class Solution:
    @classmethod
    def groupAnagrams(cls, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in anagram_map:
                anagram_map[key] = []
            anagram_map[key].append(s)
        return list(anagram_map.values())


if __name__ == '__main__':
    print(Solution.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
