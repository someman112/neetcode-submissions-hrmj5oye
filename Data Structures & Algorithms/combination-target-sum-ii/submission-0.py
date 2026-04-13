class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()
        def eval_combs(index, curr, tgt):
            if tgt == 0:
                res.append(curr[:])
                return 
            
            elif tgt < 0:
                return

            
            for i in range(index, len(candidates)):

                if i == index or candidates[i] != candidates[i-1]:                    
                    first = candidates[i]
                    curr.append(first)
                    eval_combs(i+1, curr, tgt - first)
                    curr.pop()

        eval_combs(0,[], target)
        return res
        