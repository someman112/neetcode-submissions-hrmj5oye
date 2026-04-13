class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        i1,i2=0,0
        l1,l2=len(s),len(t)
        common=0

        while i1<l1 and i2<l2:
            if s[i1]==t[i2]:
                common+=1
                i2+=1
            i1+=1
        return l2-common