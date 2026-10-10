class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '-' + s 
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            temp=""
            save = i
            while s[i] != '-':
                i += 1
            stop = i + int(s[save:i])
            while i < stop:
                i+=1
                temp += s[i]
            res.append(temp)
            i+=1
        return res

        