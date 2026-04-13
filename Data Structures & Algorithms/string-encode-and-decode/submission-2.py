class Solution:

    def encode(self, strs: List[str]) -> str:
        strr = ''

        for i in strs:
            strr+= f"{len(i)}#" + i
        
        return strr

    def decode(self, s: str) -> List[str]:
        i = 0
        lst = []
        while i < len(s):
            j = i
            while s[j].isnumeric():
                j+=1

            lenn = int(s[i:j])
            i+= (j-i)+1
            lst.append(s[i:i+lenn])
            i+=lenn

        return lst 

