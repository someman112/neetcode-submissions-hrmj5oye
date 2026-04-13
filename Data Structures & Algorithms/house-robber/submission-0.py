class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        
        prev1 = nums[0]
        prev2 = nums[0] if nums[0] > nums[1] else nums[1]

        for i in range(2, len(nums)):
            val_i = max(nums[i] + prev1, prev2)

            prev1, prev2 = prev2, val_i
        
        return prev2
        