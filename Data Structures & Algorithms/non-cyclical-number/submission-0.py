class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        curr_n = 0

        while n:
            curr_n+=(n%10)**2
            n = n // 10

            if n == 0:
                if curr_n == 1:
                    return True
                elif curr_n in seen:
                    return False

                seen.add(curr_n)
                n,curr_n = curr_n,0
        