class TrieNode:
    def __init__(self):
        self.childern={}
        self.isWord=False


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        cache = {len(s):0}
        root = TrieNode()
        for w in dictionary:
            curr=root
            for c in w:
                if c not in curr.childern:
                    curr.childern[c] = TrieNode()
                curr=curr.childern[c]
            curr.isWord=True
        

        def dfs(i):
            if i in cache: return cache[i] 

            res = 1 + dfs(i+1)
            curr=root
            j = i

            while j<len(s) and s[j] in curr.childern:
                curr=curr.childern[s[j]]
                j+=1
                if curr.isWord:
                    res = min(res, dfs(j))
            
            cache[i] = res
            return res
        
        return dfs(0)




        