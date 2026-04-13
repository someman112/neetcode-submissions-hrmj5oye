class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        cur_sum = 0

        for n in nums:
            cur_sum+=n

            res = max(cur_sum, res)

            cur_sum = max(0, cur_sum)

        return res
        
        