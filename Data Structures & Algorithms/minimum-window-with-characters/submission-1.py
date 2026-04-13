from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m,n = len(s), len(t)
        if n > m:
            return ""

        output, winsize = "", float("inf")
        l,r = 0, 0
        fs,ft = {}, Counter(t)
        have, need = 0, len(ft)

        while r < m:
            fs[s[r]] = fs.get(s[r], 0)+1
            if s[r] in ft and fs[s[r]] == ft[s[r]]:
                have+=1

            while have == need:
                if (r - l + 1) < winsize:
                    winsize = r - l + 1
                    output = s[l:r+1]
                
                fs[s[l]]-=1
                if s[l] in ft and ft[s[l]] > fs[s[l]]:
                    have -=1

                l+=1

            r+=1

        return output
        

            


        




        