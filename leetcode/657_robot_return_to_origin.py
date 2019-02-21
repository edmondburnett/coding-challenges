#!/usr/bin/env python

"""There is a robot starting at position (0, 0), the origin, on a 2D plane.
Given a sequence of its moves, judge if this robot ends up at (0, 0) after it
completes its moves.
"""


class Solution:
    def judgeCircle(self, moves: 'str') -> 'bool':
        x = 0
        y = 0
        for dir in moves:
            if dir == "U":
                y += 1
            if dir == "D":
                y -= 1
            if dir == "L":
                x -= 1
            if dir == "R":
                x += 1
        if x == 0 and y == 0:
            return True
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.judgeCircle("LR"))
