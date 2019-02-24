#!/usr/bin/env python

"""Given a binary matrix A, we want to flip the image horizontally, then invert
it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.
For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced
by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].
"""

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
