class TrieNode:
    def __init__(self):
        self.alphas = {}
        self.end = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.alphas:
                curr.alphas[c] = TrieNode()
            curr = curr.alphas[c]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.alphas:
                return False
            curr = curr.alphas[c]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.alphas:
                return False
            curr = curr.alphas[c]
        return True