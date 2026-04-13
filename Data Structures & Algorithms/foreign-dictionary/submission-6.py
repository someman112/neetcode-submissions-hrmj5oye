class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:[] for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            if len(w1) > len(w2) and w1[:len(w2)] == w2: return ""

            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    break

        state = defaultdict(int)  # 0: not visited, 1: visiting, 2: visited
        res = []
        def dfs(c):
            if state[c] == 2: return True
            if state[c] == 1: return False

            state[c] = 1  # visiting
            for child in adj[c]:
                if not dfs(child):
                    return False
            state[c] = 2  # visited

            res.append(c)
            return True



        for char in adj:
            if state[char] == 0:
                if not dfs(char): return ""
                

        res.reverse()
        return "".join(res)




            


            
        