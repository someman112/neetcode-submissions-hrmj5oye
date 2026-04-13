class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def recurse(i, amnt):
            if i == len(nums):
                return 1 if amnt == target else 0 
            
            

            return recurse(i+1, amnt+ -nums[i]) + recurse(i+1, amnt+nums[i])
        
        return recurse(0, 0)