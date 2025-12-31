#!/usr/bin/env python


# Best Time to Buy and Sell Stock
# https://neetcode.io/problems/buy-and-sell-crypto/question?list=blind75

# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

# Algorithm type: Greedy/single-pass; Sliding Window precursor


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """Brute force solution"""
        best = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > best:
                    best = profit
        return best

    def maxProfitSlidingWindow(self, prices: list[int]) -> int:
        """Single-pass solution"""
        if not prices:
            return 0

        min_price = prices[0]  # track the lowest price seen
        best = 0  # track the best profit found

        for price in prices:
            # Update the minimum if we found a lower price
            min_price = min(min_price, price)

            # Calculate profit if we sell at current price
            profit = price - min_price

            # Update the maximum profit if this is better
            best = max(best, profit)

        return best


sol = Solution()
assert sol.maxProfit([7,1,5,3,6,4]) == 5  # Buy at 1, sell at 6
assert sol.maxProfit([7,6,4,3,1]) == 0    # Prices only decrease
assert sol.maxProfit([1,2,3,4,5]) == 4    # Buy at 1, sell at 5
assert sol.maxProfit([2,4,1]) == 2        # Buy at 2, sell at 4
assert sol.maxProfit([3,3,3]) == 0        # All same price

assert sol.maxProfitSlidingWindow([7,1,5,3,6,4]) == 5  # Buy at 1, sell at 6
assert sol.maxProfitSlidingWindow([7,6,4,3,1]) == 0    # Prices only decrease
assert sol.maxProfitSlidingWindow([1,2,3,4,5]) == 4    # Buy at 1, sell at 5
assert sol.maxProfitSlidingWindow([2,4,1]) == 2        # Buy at 2, sell at 4
assert sol.maxProfitSlidingWindow([3,3,3]) == 0        # All same price

print("All tests passed!")
