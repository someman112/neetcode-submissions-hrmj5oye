class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def recurse(i, j):
            if j == len(t):
                return 1
                
            if len(s) - i  < len(t) - j or i>=len(s):
                return 0
            
            res = 0
            if s[i] == t[j]:
                res+= recurse(i+1,j+1)
            
            res+=recurse(i+1, j)
        
            return res
        
        return recurse(0,0)
        