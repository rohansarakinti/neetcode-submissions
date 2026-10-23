class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = ((r - l) // 2) + l
            midnum = nums[mid]
            if target == midnum:
                return mid
            if target < midnum:
                r = mid - 1
            else:
                l = mid + 1
        return -1