class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Space O(N) since we store nums in a hashmap for later searches for a pair.
        Time is O(N) since we linearly traverse nums to see if we already have explored a corresponding number that would add up to target.
        '''
        hs = {}
        for i in range(len(nums)):
            n = nums[i]
            if target - n in hs:
                return [hs[target - n], i]
            hs[n] = i
        return [0, 0]
