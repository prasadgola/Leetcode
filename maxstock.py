class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        idx_min = 0
        min_p = 10000
        profit = 0
        for idx, p in enumerate(prices):
            iter_profit = 0
            if p < min_p:
                min_p = p
                idx_min = idx
            if p > min_p:
                iter_profit = p-min_p
            if iter_profit>profit: profit = iter_profit
        return profit