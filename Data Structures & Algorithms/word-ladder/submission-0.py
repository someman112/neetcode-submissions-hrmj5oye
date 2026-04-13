from collections import defaultdict
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0 


        word_dict = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + "*" + word[i+1:]
                word_dict[key].append(word)
        
        q = deque([beginWord])
        visited = set([beginWord])
        res = 1
        while q:

            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res 
                    

                for j in range(len(word)):
                    key = word[:j] + "*" + word[j+1:]

                    for nei in word_dict[key]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
                
            res+=1
        return 0 