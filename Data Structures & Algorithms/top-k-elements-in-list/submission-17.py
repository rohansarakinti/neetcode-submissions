class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        O(N) time compplexity since we linearly put them in freq buckets then we linearly traverse the buckets till we get our k most frequent, but this k is also bounded by N so it becomes O(N + N) which is just O(N)

        O(N) space complexity since the max frequency we can have is the number of elements in the list and we spread the existing N numbers among buckets. We also haev a frequency map with max n keys for n frequencies.
        '''

        freqmap = {}
        for n in nums:
            freqmap[n] = freqmap.get(n, 0) + 1
        buckets = [0] * (len(nums) + 1)
        for key, v in freqmap.items():
            if buckets[v] == 0:
                buckets[v] = []
            buckets[v].append(key)
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            b = buckets[i]
            if b == 0: continue
            for n in b:
                res.append(n)
                if len(res) == k:
                    return res

