class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Space O(1) just store 2 vars
        Time O(N) linearly traverse through prices
        '''
        res, mymin = 0, prices[0]
        for p in prices:
            mymin = min(mymin, p)
            res = max(res, p - mymin)
        return res