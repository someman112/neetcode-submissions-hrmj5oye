class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        dp = [1,1]

        for i in range(1, len(s)):
            a = dp[i] if s[i] != "0" else 0
            b = dp[i-1] if s[i-1] != "0" and 10 <= int(s[i-1:i+1]) <= 26 else 0

            dp.append(a + b)
        
        return dp[-1]