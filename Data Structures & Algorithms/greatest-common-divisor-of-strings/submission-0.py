class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2) < len(str1): str1,str2=str2,str1
        l1,l2= len(str1), len(str2)

        res = ""
        for i in range(l1):
            strr = str1[:i+1]
            if l1 % (i+1) == l2 % (i+1) == 0:
                f1 = l1 // (i+1)
                f2 = l2 // (i+1)
                if strr * f1 == str1 and strr * f2 == str2:
                    res = strr
        
        return res