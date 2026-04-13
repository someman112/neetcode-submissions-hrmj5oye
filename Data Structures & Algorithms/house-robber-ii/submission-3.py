class Solution:
    def rob(self, nums: List[int]) -> int:
        def r0b(nums):
            prev1, prev2 = nums[0], max(nums[0], nums[1])

            for i in range(2, len(nums)):
                prev1, prev2 = prev2, max(nums[i] + prev1, prev2)
            
            return prev2
        

        if len(nums) < 3:
            return max(nums)
        
        a = r0b(nums[1:])
        b = r0b(nums[:len(nums)-1])
        return max(a,b)
        