class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        mydic = {'(':')', '{':'}', '[':']'}
        for c in s:
            if c in mydic:
                arr.append(c)
            else:
                if arr:
                    if mydic[arr[-1]] != c:
                        return False
                    arr.pop()
                else:
                    return False
        if arr:
            return False
        return True