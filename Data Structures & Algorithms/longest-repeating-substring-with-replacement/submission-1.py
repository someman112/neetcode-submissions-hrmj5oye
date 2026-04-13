class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        N = len(s)
        freq = {}
        maxf = 0
        l = 0
        ans = 0

        for r in range(N):

            freq[s[r]] = freq.get(s[r], 0) + 1
            maxf = max(maxf, freq[s[r]])

            if (r - l + 1) - maxf <= k:
                ans = max(ans, (r - l)+1)
            
            else:
                freq[s[l]] = freq[s[l]] - 1
                l+=1
        
        return ans
        