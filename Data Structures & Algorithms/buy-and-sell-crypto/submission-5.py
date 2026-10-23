class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mymin, best = prices[0], 0
        for i, p in enumerate(prices):
            if p < mymin:
                mymin = p;
            best = max(p - mymin, best)
        return best
            