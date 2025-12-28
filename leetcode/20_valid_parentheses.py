#!/usr/bin/env python

# https://leetcode.com/problems/valid-parentheses/description/
# https://neetcode.io/problems/validate-parentheses/question?list=blind75


class Solution:
    @classmethod
    def isValid(self, s: str) -> bool:
        opening = ["(", "{", "["]
        closing = [")", "}", "]"]
        stack = []

        for char in s:
            if char in opening:
                stack.append(char)
            if char in closing:
                if not stack:
                    # make sure stack is not empty
                    return False
                # get the index of the corresponding closing paren
                closing_index = closing.index(char)
                if stack[-1] != opening[closing_index]:
                    return False
                # remove the opening paren from the stack
                stack.pop()
        
        # make sure stack is empty at the end (all valid pairs handled)
        return len(stack) == 0


if __name__ == '__main__':
    print(Solution.isValid("[]"))
    print(Solution.isValid("([{}])"))
    print(Solution.isValid("([{)"))
