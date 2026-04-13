class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:[] for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return ""

            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    break

        state = defaultdict(int)  # 0: not visited, 1: visiting, 2: visited
        res = []
        def dfs(c):
            if state[c]:
                return state[c]

            state[c] = 1  # visiting

            for child in adj[c]:
                val = dfs(child)
                if val==1:
                    return val

            state[c] = 2  # visited
            res.append(c)



        for char in adj:
            if state[char] == 0:
                val = dfs(char)
                if val == 1:
                    return ""

        res.reverse()
        return "".join(res)




            


            
        