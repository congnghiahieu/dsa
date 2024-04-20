class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price_idx, max_profix = 0, 0
        for i in range(1, len(prices)):
            if prices[i] < prices[min_price_idx]:
                min_price_idx = i
            else:
                max_profix = max(max_profix, prices[i] - prices[min_price_idx])

        return max_profix
