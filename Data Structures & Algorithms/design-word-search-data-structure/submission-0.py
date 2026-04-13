class TrieNode:
    def __init__(self):
        self.vals = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for i, c in enumerate(word):
            
            if c in curr.vals:
                curr = curr.vals[c]
            else:
                curr.vals[c] = TrieNode()
                curr = curr.vals[c]
        
        curr.end = True
        
    def search(self, word: str) -> bool:
        
        def dfs(i, node):
            if i == len(word):
                return node.end

            if not node.vals:
                return False
            
            if word[i] != ".":
                return word[i] in node.vals and dfs(i+1, node.vals[word[i]])
                
            if word[i] == '.':
                return any(dfs(i+1, child) for child in node.vals.values())
        
        return dfs(0, self.root)