class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Space complexity: O(N) where n is max(len(s), len(t)) since you have to store all the characters in frequency maps for each string
        # Time complexity: O(N) how to iterate through each index available in the max strings
        hs, ht = {}, {}
        maxlen = max(len(s), len(t))
        for i in range(maxlen):
            if i < len(s):
                hs[s[i]] = hs.get(s[i], 0) + 1
            if i < len(t):
                ht[t[i]] = ht.get(t[i], 0) + 1
        return hs == ht