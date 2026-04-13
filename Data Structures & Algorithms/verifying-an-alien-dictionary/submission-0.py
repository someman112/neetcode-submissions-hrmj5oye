class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        chars={}
        for i in range(len(order)):
            chars[order[i]] = i
        

        for idx in range(len(words)-1):
            w1,w2 = words[idx],words[idx+1]
            if len(w1) > len(w2) and w1[:len(w2)] == w2: return False

            for i in range(min(len(w1), len(w2))):
                if w1[i] != w2[i]:
                    if chars[w1[i]] > chars[w2[i]]: return False
                    break
                    
            
        return True


