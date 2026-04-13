class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        cntr = Counter(nums)
        ans, perm = [], []

        def dfs():
            if len(perm) == len(nums):
                ans.append(perm[:])
                return 
            

            for n in cntr:
                if cntr[n]>0:
                    perm.append(n)
                    cntr[n]-=1

                    dfs()

                    perm.pop()
                    cntr[n]+=1
            
        dfs()
        return ans
        