class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        hp = []
        for char, cnt in [("a", a), ("b", b), ("c", c)]:
            if cnt>0: heapq.heappush(hp, (-cnt, char))
        
        res = ""

        while hp:
            cnt, char = heapq.heappop(hp)
            cnt*=-1

            if len(res)>=2 and res[-2] == res[-1] == char:
                
                if not hp: return res
                cnt2, char2 = heapq.heappop(hp)
                cnt2*=-1
                res+=char2
                cnt2-=1
                if cnt2: heapq.heappush(hp, (-cnt2, char2))
                heapq.heappush(hp, (-cnt, char))
                continue 
            
            res+=char
            cnt-=1
            if cnt>0: heapq.heappush(hp, (-cnt, char))
        
        return res