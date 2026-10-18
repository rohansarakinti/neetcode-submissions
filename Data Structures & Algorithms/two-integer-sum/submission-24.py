class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time Complexity: O(N) search through nums while searching if its matching number has been detected or not already
        # Space complexity: O(N) have to store all past nums encountered and their corresponding index
        hm = {}
        for i in range(len(nums)):
            n = nums[i]
            if target - n in hm:
                return [hm[target - n], i]
            hm[n] = i
        return [0, 0]