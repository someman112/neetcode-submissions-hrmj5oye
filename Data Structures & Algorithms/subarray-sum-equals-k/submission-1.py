from collections import Counter

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pfxsm = defaultdict(int)
        pfxsm[0] = 1
        curr_sum = 0
        res = 0
        
        for i in nums:
            curr_sum+=i

            if curr_sum - k in pfxsm:
                res+=pfxsm[curr_sum - k]
            
            pfxsm[curr_sum]+=1
        return res


