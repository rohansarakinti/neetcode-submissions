class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        Hashset to track dups O(N) space
        Linear traversal O(N)
        '''
        hs = set()
        for n in nums:
            if n in hs:
                return True
            hs.add(n)
        return False