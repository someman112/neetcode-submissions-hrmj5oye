class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def count(i,j):
            cnt = 0
            while 0 <= i <= j < len(s) and s[i] == s[j]:
                cnt+=1
                i,j = i-1, j+1
            return cnt
            
        
        for i in range(len(s)):
            res+=count(i,i)
        
        for i in range(len(s)-1):
            res+=count(i, i+1)
        
        return res
        