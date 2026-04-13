class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def doable(weight):
            dcnt, summ = 1, 0
            for i in weights:
                if summ+i>weight:
                    summ = 0
                    dcnt+=1
                summ+=i
            return dcnt<=days
        
        start, end = max(weights), sum(weights)


        while start<end:
            mid = (start+end) // 2

            if doable(mid):
                end = mid
            
            else:
                start = mid+1
        
        return start # or return end, they're the same



        
        