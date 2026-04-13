class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        N = min(len(word1), len(word2))
        i = 0

        while i < N:
            s+= word1[i]
            s+= word2[i]
            i+=1
        
        s+= word1[i:]
        s+= word2[i:]

        return s