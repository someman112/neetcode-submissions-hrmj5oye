# for some n
# -> n%26 (last digit) 
# -> n//26 (prefix)
# ==> valid when digits \in [0 to 25] ==> must normalize by subtracting 1

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        mapping = {i: c for i, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}

        res = ''
        while columnNumber > 0:
            last_digit = (columnNumber-1) % 26
            prefix= (columnNumber-1) // 26

            res=mapping[last_digit] + res
            columnNumber=prefix

        return res