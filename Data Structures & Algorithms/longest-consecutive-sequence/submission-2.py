class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        output = 0
        num_set = set(nums)

        for i in nums:
            if (i-1) in num_set:
                continue
            
            curr_output = 1
            curr_num = i+1
            
            while True:
                if (curr_num) in num_set:
                    curr_num+=1
                    curr_output+=1
                else:
                    break
            if curr_output > output:
                output = curr_output

        return output 

                    
                    




        