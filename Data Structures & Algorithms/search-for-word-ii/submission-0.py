class TrieNode:

    def __init__(self):
        self.vals = {}
        self.end = ""


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        curr = self.root

        for c in word:
            if c not in curr.vals:
                curr.vals[c] = TrieNode()
            curr = curr.vals[c]
            
        curr.end = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m,n = len(board), len(board[0])
        wd = Trie()
        for w in words:
            wd.addWord(w)

        output, visited = [], set()

        def dfs(i,j, node):
            if (i>=m or i<0) or (j>=n or j<0) or (i, j) in visited or board[i][j] not in node.vals:
                return
            
            child = node.vals[board[i][j]]
            if child.end != "":
                output.append(child.end)
                child.end = ""
            
            visited.add((i,j))

            for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
                dfs(i+di, j+dj, child)
            
            visited.remove((i,j))
        
        for i in range(m):
            for j in range(n):
                dfs(i,j, wd.root)
        
        return output

            



        

















        