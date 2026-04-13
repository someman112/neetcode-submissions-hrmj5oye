class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prod = 1
        output = [1] * len(nums)


        for i in range(len(nums)):
            output[i] = prod
            prod*= nums[i]

        prod = 1

        for i in range(len(nums) -1, -1, -1):
            output[i] = prod  * output[i]
            prod *= nums[i]

        return output

        






        