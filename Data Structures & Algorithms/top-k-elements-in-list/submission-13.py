class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        buckets = []
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
            buckets.append([])
        buckets.append([])
        
        
        for key, v in freq.items():
            buckets[v].append(key)

        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for t in buckets[i]:
                res.append(t)
                if len(res) == k:
                    return res
            
        