class Solution:
    def trap(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1
        maxL = height[0]
        maxR = height[r]
        output = []


        while l < r:

            if maxL < maxR:
                l+=1
                output.append(max((min(maxL, maxR) - height[l]), 0))
                maxL = max(maxL, height[l])

            else:
                r-=1
                output.append(max((min(maxL, maxR) - height[r]), 0))
                maxR = max(maxR, height[r])
        
        return sum(output)





        