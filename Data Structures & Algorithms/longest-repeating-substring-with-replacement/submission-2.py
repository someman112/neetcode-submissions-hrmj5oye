class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        l,r = 0, 0
        mf = 0
        res = 0

        while r < len(s):
            window[s[r]]+=1
            mf = max(mf, window[s[r]])
            r+=1

            while (r - l) - mf > k:
                window[s[l]]-=1
                l+=1
            
            res = max(res, r - l)
        
        return res



        