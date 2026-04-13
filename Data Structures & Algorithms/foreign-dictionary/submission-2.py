class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list = {c:set() for word in words for c in word}

        for i in range(len(words)-1):
            w1,w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            for j in range(minLen):
                if w1[j]!= w2[j]:
                    adj_list[w1[j]].add(w2[j])
                    break
        
        res = []
        state = {}

        def dfs(n):
            if n in state:
                return state[n]
            
            state[n] = True
            for nei in adj_list[n]:
                if dfs(nei):
                    return True
            state[n] = False

            res.append(n)
        
        for c in adj_list:
            if dfs(c):
                return ""
            
        res.reverse()

        return "".join(res)
        




        