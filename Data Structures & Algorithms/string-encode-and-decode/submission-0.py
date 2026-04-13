class Solution:

    def encode(self, strs: List[str]) -> str:

        s = ''

        for st in strs:
            s+= str(len(st)) + '##'
            s+=st
        
        return s

    def decode(self, s: str) -> List[str]:

        lst = []
        idx = 0

        while idx < len(s):
            lenn = ''

            while s[idx].isdigit():
                lenn+= s[idx]
                idx+=1

            lenn = int(lenn)
            idx+=2

            lst.append(s[idx:idx+lenn])
            idx+=lenn
        return lst











