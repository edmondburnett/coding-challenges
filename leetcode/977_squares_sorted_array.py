#!/usr/bin/env python

"""Given an array of integers A sorted in non-decreasing order, return an array
of the squares of each number, also in sorted non-decreasing order.
"""
from typing import List


class Solution:
    def sortedSquares(self, A: 'List[int]') -> 'List[int]':
        squares = []
        for i in A:
            squares.append(i**2)
        squares.sort()
        return squares

    def sortedSquares2(self, A: 'List[int]') -> 'List[int]':
        return sorted(i * i for i in A)

    def sortedSquares3(self, A: 'List[int]') -> 'List[int]':
        squares = [0] * len(A)
        l = 0
        r = len(A) - 1
        while l <= r:
            left = abs(A[l])
            right = abs(A[r])
            print(f"Left {left}, Right: {right}, L: {l}, R: {r}")
            if left > right:
                squares[r - l] = left * left
                l += 1
            else:
                squares[r - l] = right * right
                r -= 1
        return squares


if __name__ == '__main__':
    sol = Solution()
    print(sol.sortedSquares([-4, -1, 0, 3, 10]))
    print(sol.sortedSquares([-7, -3, 2, 3, 11]))

    print(sol.sortedSquares2([-4, -1, 0, 3, 10]))
    print(sol.sortedSquares2([-7, -3, 2, 3, 11]))

    print(sol.sortedSquares3([-4, -1, 0, 3, 10]))
    print(sol.sortedSquares3([-7, -3, 2, 3, 11]))
