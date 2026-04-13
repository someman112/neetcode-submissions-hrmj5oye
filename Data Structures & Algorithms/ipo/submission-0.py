class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        data=sorted([(capital[i], profits[i]) for i in range(len(profits))])
        n=len(data)
        i,j,res=0,0,w
        hp=[]

        while i<k:

            while j<n and data[j][0]<=res:
                heapq.heappush(hp, (-data[j][1], data[j][0]))
                j+=1
            
            if not hp: return res
            
            profit,cost = heapq.heappop(hp)
            profit*=-1
            res+=profit
            i+=1
        
        return res
            


