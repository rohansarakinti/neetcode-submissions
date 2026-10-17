class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Time complexity: O(N) - we maintain a left and right pointer which check the corresponding alphanumeric left and right character. 
        Space complexity: O(1) since you just need 2 pointers to do this no matter the size
        Problems: This implementation is uncessarily complex 
        """ 
        s = s.lower()
        r, l = len(s) - 1, 0
        while l < r:
            while (l < len(s) and s[l].isalnum() == False):
                l += 1
            while (r > 0 and s[r].isalnum() == False):
                r -= 1
            if l < r:
                if s[l] != s[r]:
                    return False
            l += 1
            r -= 1
        return True
        