class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l, r = 0, 0
        res = 0 

        while r < len(s):

            if s[r] in seen:
                idx = seen[s[l]]

                while l <= idx:
                    del seen[s[l]]
                    l+=1
            
            else:
                seen[s[r]] = r
                r+=1
                res = max(res, r - l)
                
                
        
        return res
        