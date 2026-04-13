class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum,min_sum = nums[0], nums[0]
        curr_min, curr_max = nums[0], nums[0]

        for i in range(1,len(nums)):
            if curr_max < 0: curr_max=0
            if curr_min > 0: curr_min=0
            curr_min+=nums[i]
            curr_max+=nums[i]
            max_sum=max(max_sum, curr_max)
            min_sum=min(min_sum, curr_min)

        if max_sum < 0: return max_sum
        return max(max_sum, sum(nums)-min_sum)