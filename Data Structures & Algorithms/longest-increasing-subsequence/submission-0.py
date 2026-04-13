class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        res = 1

        for i in range(len(nums)):

            for j in range(0, i):

                if nums[j] < nums[i]:
                    dp[i] = dp[i] if dp[i] > 1 + dp[j] else 1 + dp[j]
                    res = res if res > dp[i] else dp[i]
        
        return res
        