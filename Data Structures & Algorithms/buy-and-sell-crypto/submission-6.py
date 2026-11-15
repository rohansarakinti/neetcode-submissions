class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, mymin = 0, prices[0]
        for p in prices:
            mymin = min(mymin, p)
            res = max(res, p - mymin)
        return res