class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        lst = defaultdict(lambda: [0, 0])

        for a,b in trust:
            lst[a][0]+=1
            lst[b][1]+=1
        
        for k in range(1, n+1):
            if lst[k][0] == 0 and lst[k][1] == n-1:
                return k
            
        
        return -1