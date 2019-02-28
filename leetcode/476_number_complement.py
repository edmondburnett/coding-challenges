#!/usr/bin/env python

"""Given a positive integer, output its complement number. The complement
strategy is to flip the bits of its binary representation.
"""


class Solution:
    def findComplement(self, num: int) -> int:
        binary = str(bin(num))[2:]
        flipped = ""
        for i in range(len(binary)):
            if binary[i] == '0':
                flipped = flipped + "1"
            elif binary[i] == '1':
                flipped = flipped + "0"
        return int(flipped, 2)


if __name__ == "__main__":
    sol = Solution()
    print(sol.findComplement(15))
