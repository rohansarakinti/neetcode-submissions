class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        mydic = {'(':')', '{':'}', '[':']'}
        for c in s:
            if c in mydic:
                arr.append(c)
            else:
                if (not arr) or mydic[arr[-1]] != c:
                    return False
                arr.pop()
                
        if arr:
            return False
        return True