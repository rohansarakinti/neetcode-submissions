class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ss = {}
        st = {}
        for i in range(len(s)):
            schar = s[i]
            tchar = t[i]
            ss[schar] = ss.get(schar, 0) + 1
            st[tchar] = st.get(tchar, 0) + 1

        return ss == st