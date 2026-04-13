class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        
        def eval_combs(index, curr, tgt):
            if tgt == 0:
                res.append(curr + [])
                return 
            
            elif tgt < 0:
                return 

            
            for i in range(index, len(nums)):
                curr.append(nums[i])
                eval_combs(i, curr, tgt - nums[i])
                curr.pop()
        
        eval_combs(0,[], target)

        return res
        