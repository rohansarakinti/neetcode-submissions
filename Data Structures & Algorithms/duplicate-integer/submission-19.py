class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ms = set()
        for n in nums:
            if n in ms:
                return True
            else:
                ms.add(n)
        return False