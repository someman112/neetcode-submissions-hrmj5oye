class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        curr_num = None

        for i in range(len(nums)):

            if nums[i]!=curr_num:
                nums[idx]=nums[i]
                idx+=1
                curr_num = nums[i]
        return idx 
        