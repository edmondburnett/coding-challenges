#!/usr/bin/env python

"""Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged = list(address)
        count = 0
        for index, char in enumerate(address):
            if char == '.':
                defanged.insert(index + count, '[')
                defanged.insert(index + count + 2, ']')
                count = count + 2
        return ''.join(defanged)



if __name__ == '__main__':
    s = Solution()
    print(s.defangIPaddr('192.168.100.1'))
