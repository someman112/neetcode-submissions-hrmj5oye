class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0]*len(text2) for _ in range(len(text1))]

        for i in range(len(text1)):
            for j in range(len(text2)):

                if text1[i] == text2[j]:
                    cell1 = dp[i-1][j-1] if i-1>=0 and j-1>=0 else 0
                    dp[i][j]+= 1 + cell1
                
                else:
                    cell2 = dp[i-1][j] if i-1>=0 else 0
                    cell3 = dp[i][j-1] if j-1>=0 else 0
                    dp[i][j] = max(cell2, cell3)




        return dp[-1][-1]

        