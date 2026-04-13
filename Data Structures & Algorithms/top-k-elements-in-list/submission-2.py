class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}

        for i in nums:
            freqs[i] = freqs.get(i, 0)+1
        
        return sorted(freqs, key=freqs.get, reverse=True)[:k]
        
        