class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        value = 0

        while i < j:
            val = min(heights[i], heights[j]) * abs(i - j )

            if val > value:
                value = val

            if heights[i] > heights[j]:
                j-=1
            else:
                i+=1
                
        return value 

        