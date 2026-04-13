from collections import Counter

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        crsm = 0
        count[crsm]+=1
        res = 0

        for n in nums:
            crsm+=n

            res+= count[crsm - k]
            count[crsm]+=1
        
        return res
        
