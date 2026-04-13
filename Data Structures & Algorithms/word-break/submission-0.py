class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        maxLen = max(len(i) for i in wordDict)

        dp = [True] + [False] * len(s)


        for i in range(len(s)):
            for j in range(maxLen):

                if i - j < 0:
                    break
                
                if s[i-j:i+1] in wordDict and dp[i-j]:
                    dp[i+1] = True
                
        return dp[-1]
                
            
        