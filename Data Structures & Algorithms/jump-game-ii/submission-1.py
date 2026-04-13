class Solution:
    def jump(self, nums: List[int]) -> int:
        res,curr,furthest = 0, 0, 0


        for i in range(len(nums) - 1 ):

            furthest = max(furthest, i + nums[i])

            if i == curr:
                res+=1
                curr = furthest


        return res 
        