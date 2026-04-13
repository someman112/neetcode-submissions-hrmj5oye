class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m,n = len(s1), len(s2)
        if m > n:
            return False

        f1 = {}
        f2 = {}
        l,r = 0, m
        for i in s1:
            f1[i] = f1.get(i,0)+1

        for i in s2[:r]:
            f2[i] = f2.get(i,0)+1
        
        while r < n:
            if f2 == f1:
                return True
            
            f2[s2[l]]-=1
            if f2[s2[l]] == 0:
                del f2[s2[l]]
            l+=1

            f2[s2[r]]=f2.get(s2[r], 0)+1
            r+=1
        
        return f1 == f2

        