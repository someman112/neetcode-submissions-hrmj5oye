class Solution:
    def reorganizeString(self, s: str) -> str:
        cntr = Counter(s)
        hp = []
        for k in cntr:
            heapq.heappush(hp, (-cntr[k], k))
        
        curr = None
        res = ""

        while hp:
            count, char = heapq.heappop(hp)
            count*=-1
            res+=char
            count-=1

            if curr: heapq.heappush(hp, (curr[0], curr[1]))
            if count>0: 
                curr = (-count, char)
            else:
                curr = None

        if curr: return ""
        return res
            