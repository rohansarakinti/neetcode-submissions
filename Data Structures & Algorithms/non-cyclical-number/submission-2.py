class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        Use a hashset to track seen numbers and perform operation continuously till we get the answer.
        '''
        hs = set()
        while n not in hs:
            hs.add(n)
            temp = str(n)
            n = 0
            for c in temp:
                n += int(c)**2
            if n == 1:
                return True
        return False