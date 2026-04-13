import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_eat(k):
            hh = 0
            for p in piles:
                hh+= math.ceil(p / k)

                if hh > h:
                    return False

            return True
        

        l,r = math.ceil(sum(piles) / h), max(piles)
        while l < r:
            mid = (r+l) // 2

            if can_eat(mid):
                r = mid
            else:
                l = mid+1
        
        # l == r so return either 
        return r

        



        