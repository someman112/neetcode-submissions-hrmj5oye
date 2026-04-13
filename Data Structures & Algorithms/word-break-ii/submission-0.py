class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        solns = []
        wordDict=set(wordDict)

        def dfs(start, end, curr_soln):
            
            if start >= len(s):
                solns.append(" ".join(curr_soln))
                return 
            
            if end > len(s):
                return 
            
            if s[start:end] in wordDict:
                curr_soln.append(s[start:end])
                dfs(end, end, curr_soln)
                curr_soln.pop()
            
            dfs(start, end+1, curr_soln)
        
        dfs(0,0, [])
        return solns


            


        