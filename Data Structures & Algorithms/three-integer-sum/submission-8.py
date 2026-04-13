class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums) - 1 
        
        def twosum(i, target):
            j = N
            res = []

            while i < j:
                if nums[i] + nums[j] < target:
                    i+=1
                elif nums[i] + nums[j] > target:
                    j-=1
                else:
                    res.append([nums[i], nums[j]])
                    i+=1
                    j-=1

                    while i < j and nums[i] == nums[i-1]:
                        i+=1
                    
                    while i < j and nums[j] == nums[j+1]:
                        j-=1
            
            return res

        
        ans = []
        for idx in range(N - 1):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue 

            for pair in twosum(idx+1, -nums[idx]):
                ans.append ([nums[idx]] + pair)

        
        return ans




        