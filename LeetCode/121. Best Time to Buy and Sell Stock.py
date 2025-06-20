class Solution:
    def maxProfit(self, prices: list[int]) -> int: # Changed List to list for type hint consistency
        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]: # Corrected 'price' to 'prices' to match the parameter name
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1

        return maxP