#!/usr/bin/env python


# Best Time to Buy and Sell Stock
# https://neetcode.io/problems/buy-and-sell-crypto/question?list=blind75

# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        best = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > best:
                    best = profit
        return best


sol = Solution()
assert sol.maxProfit([7,1,5,3,6,4]) == 5  # Buy at 1, sell at 6
assert sol.maxProfit([7,6,4,3,1]) == 0    # Prices only decrease
assert sol.maxProfit([1,2,3,4,5]) == 4    # Buy at 1, sell at 5
assert sol.maxProfit([2,4,1]) == 2        # Buy at 2, sell at 4
assert sol.maxProfit([3,3,3]) == 0        # All same price
print("All tests passed!")
