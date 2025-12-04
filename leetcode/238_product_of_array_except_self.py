#!/usr/bin/env python

# neetcode: https://neetcode.io/problems/products-of-array-discluding-self/question
# leetcode: https://leetcode.com/problems/product-of-array-except-self/

from typing import List

class Solution:

    @classmethod
    def productExceptSelf(cls, nums: List[int]) -> List[int]:
        output = []
        for index1, num1 in enumerate(nums):
            product = 1
            for index2, num2 in enumerate(nums):
                if index1 == index2:
                    continue
                product *= num2
            output.append(product)
        return output


if __name__ == '__main__':
    print(Solution.productExceptSelf([1,2,4,6]))
    print(Solution.productExceptSelf([-1,0,1,2,3]))
