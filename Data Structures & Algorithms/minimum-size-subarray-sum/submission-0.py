class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf") 
        l,r = 0, 0 
        summ = 0 

        while r < len(nums):
            summ+=nums[r]
            r+=1

            while summ >= target:
                res = min(res, r - l)
                summ-=nums[l]
                l+=1

        return 0 if res == float("inf") else res

        