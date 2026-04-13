class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m,n = len(num1), len(num2)
        res = [0] * (m+n)

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                mult = int(num1[i]) * int(num2[j]) 
                prev = res[i+j+1]
                mult+=prev

                res[i+j+1] = mult % 10
                res[i+j]+= mult//10
        
        res = [str(i) for i in res]
        i = 0
        while res[i] == "0":
            i+=1
        return "".join(res[i:])





        