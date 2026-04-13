class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def recurse(index, curr):
            if index>= len(nums):
                res.append(curr + [])
                return
            

            curr.append(nums[index])
            recurse(index+1, curr)            
            curr.pop()

            index+=1
            while index < len(nums) and nums[index] == nums[index-1]:
                index+=1
            recurse(index, curr)

        
        recurse(0, [])

        return res 
        