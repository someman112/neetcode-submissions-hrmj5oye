from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        for i in range(len(nums)): nums[i] = str(nums[i])
        
        def comparator(a,b):
            if int(a+b) > int(b+a):
                return -1
            elif int(a+b) < int(b+a):
                return 1
            return 0
            
        nums.sort(key=cmp_to_key(comparator))
        if nums[0]=="0":return "0"
        return "".join(nums)