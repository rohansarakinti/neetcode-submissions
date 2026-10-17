class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # O(N) since linear search through nums
        # O(N) space for hashset
        hs = set()
        for n in nums:
            if n in hs:
                return True
            hs.add(n)
        return False