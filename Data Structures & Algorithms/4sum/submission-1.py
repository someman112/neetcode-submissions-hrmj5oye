class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        N = len(nums) - 1

        def threeSum(start, target):
            res = []

            for idx in range(start, N):

                if idx > start and nums[idx] == nums[idx-1]:
                    continue 
                
                i,j= idx+1, N
                target2 = target - nums[idx]

                while i < j:
                    if nums[i] + nums[j] < target2:
                        i+=1
                    elif nums[i] + nums[j] > target2:
                        j-=1
                    
                    else:
                        res.append([nums[idx], nums[i], nums[j]])
                        i+=1
                        j-=1

                        while i < j and nums[i] == nums[i-1]:
                            i+=1
                        
                        while i < j and nums[j] == nums[j+1]:
                            j-=1
                        
            return res
        
        ans = []
        for idx in range(N):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue 
            
            for triplet in threeSum(idx+1, target - nums[idx]):
                ans.append([nums[idx]] + triplet)
            
        return ans



        