class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0


        for i, jump_val in enumerate(nums):

            if i > furthest:
                return False

            furthest = max(furthest, i + jump_val)

            if furthest >= len(nums) - 1:
                return True
                
        return True 
        