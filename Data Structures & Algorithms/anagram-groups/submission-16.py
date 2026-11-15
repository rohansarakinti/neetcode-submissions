class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Space is O(N) because we have to store max N freq maps that are each constant size due to the alphabet being max 26 chars where N is the number of strings in the strs list.
        Time is O(M * N) where M is the max character count in strs and we have to iterate over each char in each word so yea.
        '''
        hm = {}
        for s in strs:
            temp = [0] * 26
            for c in s:
                temp[ord(c) - ord('a')]+=1
            temp = tuple(temp)
            if temp not in hm:
                hm[temp] = []
            hm[temp].append(s)
        return [v for v in hm.values()]