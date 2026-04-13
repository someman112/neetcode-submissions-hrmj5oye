class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b=a[::-1],b[::-1]
        i,j = 0, 0
        carry = 0
        res=''

        while i<len(a) or j<len(b) or carry:
            num1 = int(a[i]) if i < len(a) else 0
            num2 = int(b[j]) if j < len(b) else 0
            val = num1+num2+carry
            res = str(val%2) + res
            carry = val // 2
            i+=1
            j+=1
        
        return res