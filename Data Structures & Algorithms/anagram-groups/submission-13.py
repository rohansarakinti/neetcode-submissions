class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for s in strs:
            temp = [0] * 26
            for c in s:
                temp[ord(c) - ord('a')] += 1
            temp = tuple(temp)
            if temp not in hm:
                hm[temp] = []
            hm[temp].append(s)
        res = []
        for k, v in hm.items():
            res.append(list(v))
        return res
        