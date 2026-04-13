class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]

        def recurse(i, comb):
            if len(comb)==k:
                res.append(comb[:])
                return
            
            for j in range(i, n+1):
                comb.append(j)
                recurse(j+1, comb)
                comb.pop()
        
        recurse(1, [])
        return res
        