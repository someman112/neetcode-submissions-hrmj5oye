class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        lp = 0
        rp = len(heights) - 1


        while lp  < rp:

            curr_area = min(heights[lp], heights[rp]) * (rp - lp)
            area = max(area, curr_area)

            if heights[lp] < heights[rp]:
                lp+=1
            else:
                rp-=1

        return area


            

            

            


        
        