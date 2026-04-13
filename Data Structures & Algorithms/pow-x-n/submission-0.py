class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        res = 1 
        neg = n < 0
        n = abs(n)

        while n > 0:
            if n % 2 == 1:
                res*=x
            
            x = x*x
            n = n // 2
        
        return 1/res if neg else res
        