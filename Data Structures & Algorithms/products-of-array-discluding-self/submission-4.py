class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums) 
        products = [1] * N

        prefix = 1
        for i in range(1, N):
            prefix = prefix*nums[i-1]
            products[i] = prefix

        suffix = 1
        for i in range(N-1, -1, -1):
            products[i]*=suffix
            suffix*=nums[i]
            
        return products

            
        
        