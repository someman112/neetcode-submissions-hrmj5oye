class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        ds = {}
        dt = {}

        for i in s:
            if i in ds:
                ds[i]+=1
            else:
                ds[i] = 1
        

        for i in t:
            if i in dt:
                dt[i]+=1
            else:
                dt[i] = 1

        return ds == dt
        