class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        mapping={i+1:c for i,c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}

        res=[]

        while columnNumber:
            idx=(columnNumber-1)%26+1
            res.append(mapping[idx])
            columnNumber=(columnNumber-1)//26

        return "".join(reversed(res))        