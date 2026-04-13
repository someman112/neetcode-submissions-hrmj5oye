class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        N = len(nums)

        while i < N:

            if 0 < nums[i] < N and nums[i]-1 != i and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]     
            else:
                i+=1
        
        for i in range(N):
            if nums[i] != i+1:
                return i+1
        return N+1 
        