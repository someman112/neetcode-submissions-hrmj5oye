class Solution:
    def reverse(self, x: int) -> int:
        mx = 2**31-1
        mn = -2**31

        x,neg = abs(x), x < 0
        ans, x= x % 10, x // 10

        while x:
            ans = ans*10 + (x%10)

            if not (mn<=ans<=mx):
                return 0
            
            x = x // 10
        
        return -ans if neg else ans 
        