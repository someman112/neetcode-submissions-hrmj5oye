class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0] * len(s) for _ in range(len(s))]
        res = ""
        max_l = 0

        # mark trivial palindromes (strings of length 1)
        for i in range(len(s)):
            dp[i][i] = 1
            res = s[i]
        
        # mark all palindromes of length 2
        for i in range(1,len(s)):
            if s[i-1] == s[i]:
                dp[i-1][i] = 1
                res = s[i-1:i+1]
        
        for l in range(3, n+1):
            for i in range(n - l + 1):
                j = l + i - 1

                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = 1

                    if l > max_l:
                        res = s[i:j+1]
                        max_l = l
        
        return res
        