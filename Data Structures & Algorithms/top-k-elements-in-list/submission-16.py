class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # create frequency map
        freqmap = {}
        for n in nums:
            freqmap[n] = freqmap.get(n, 0) + 1
        # create buckets for bucket sort
        buckets = [None] * (len(nums) + 1)
        for key, v in freqmap.items():
            if buckets[v] is None:
                buckets[v] = []
            buckets[v].append(key)
        # create result array
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            if buckets[i] is None:
                continue
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
            
