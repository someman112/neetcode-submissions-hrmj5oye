class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        N = len(heights)
        i, max_arr = 0, 0


        for i in range(N):
            start_idx = i

            while stack and stack[-1][0] > heights[i]:

                height, index = stack.pop()                
                curr_area = (i - index) * height
                
                max_arr = max(max_arr, curr_area)
                start_idx = index

            stack.append((heights[i], start_idx))


        for height, index in stack:
            curr_area = (N - index) * height
            max_arr = max(max_arr, curr_area) 

        return max_arr
        