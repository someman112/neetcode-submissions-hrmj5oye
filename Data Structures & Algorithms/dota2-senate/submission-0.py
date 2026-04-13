class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q1=deque([])
        q2=deque([])
        n = len(senate)

        for i in range(n):
            if senate[i]=="R": q1.append(i)
            if senate[i]=="D": q2.append(i)
        
        while q1 and q2:
            i1 = q1.popleft()
            i2 = q2.popleft()

            if i1 < i2:
                q1.append(i1+n)
            else:
                q2.append(i2+n)
        
        if q1 and not q2: return "Radiant"
        return "Dire"