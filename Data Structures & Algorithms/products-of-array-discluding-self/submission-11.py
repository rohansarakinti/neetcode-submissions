class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        [1, 1, 2, 8, 48]
        [48, 24, 6, 1, 48]
        '''
        # pre arr - running prod up to i
        pre = [1] * (len(nums) + 1)
        for i in range(len(nums)):
            pre[i + 1] = pre[i] * nums[i]
        # suff arr - running prod up to i backwards
        suff = [1] * (len(nums) + 1)
        for i in range(len(nums) - 1, -1, -1):
            suff[i] = suff[i + 1] * nums[i]
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = pre[i] * suff[i + 1]
        return res
