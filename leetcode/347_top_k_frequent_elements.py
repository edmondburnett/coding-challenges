#!/usr/bin/env python

# https://leetcode.com/problems/top-k-frequent-elements/description/
# https://neetcode.io/problems/top-k-elements-in-list/question?list=blind75

from typing import List

class Solution:
    @classmethod
    def topKFrequent(cls, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            if num not in freq_map:
                freq_map[num] = 0
            freq_map[num] += 1
        s = sorted(freq_map, key=freq_map.get, reverse=True)
        return s[0:k]


if __name__ == '__main__':
    print(Solution.topKFrequent([1,2,2,3,3,3], 2))
    print(Solution.topKFrequent([7,7], 1))
