class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        hp=[]
        time=0
        curr_pass=0
        i=0

        while i<len(trips):
            while hp and time>=hp[0][0]:
                curr_pass-=hp[0][1]
                heapq.heappop(hp)

            np,frm,to=trips[i]
            
            if time<frm:
                time+=1
            elif time == frm:
                if curr_pass+np>capacity: return False
                curr_pass+=np
                heapq.heappush(hp, (to, np))
                i+=1
        
        return True