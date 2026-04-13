class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product = 1
        zeros = []
        ans = []

        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(i)
            else:
                product*=nums[i]


        if not zeros:
            for i in range(len(nums)):
                ans.append(product // nums[i])

        elif len(zeros) == 1:
            for i in range(len(nums)):
                if i in zeros:
                    ans.append(product)
                else:
                    ans.append(0)
        else:
            return [0]*len(nums)
        
        
        return ans




        