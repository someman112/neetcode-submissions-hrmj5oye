class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cntr = 1
        curr_num = nums[0]

        for num in nums[1:]:
            if num==curr_num:
                cntr+=1
            else:
                cntr-=1
            
            
            if not cntr:
                curr_num = num
                cntr = 1
        
        return curr_num
        