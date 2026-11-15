class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Construct freq maps for s and t then compare.
        time complexity is O(N + M) where N is the no of chars in s and M is the no of chars in t, space complexity is O(1) since max 26 chars in alphabet
        '''
        if len(s) != len(t):
            return False

        freqS, freqT = {}, {}

        for i in range(len(s)):
            schar, tchar = s[i], t[i]
            freqS[schar] = freqS.get(schar, 0) + 1
            freqT[tchar] = freqT.get(tchar, 0) + 1
        
        return freqS == freqT