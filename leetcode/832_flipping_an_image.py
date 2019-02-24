#!/usr/bin/env python

from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            # reverse the lists
            row.reverse()
            for i in range(len(row)):
                # invert the numbers
                if row[i] == 0:
                    row[i] = 1
                else:
                    row[i] = 0
        return A



if __name__ == '__main__':
    sol = Solution()
    print(sol.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
    print(sol.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
