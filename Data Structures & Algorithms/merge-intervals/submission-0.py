class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = []
        li = len(intervals)
        i = 0

        while i < li:
            start, end = intervals[i][0], intervals[i][1]
            j = i+1
            
            while j < li and intervals[j][0] <= end:
                start = min(start, intervals[j][0])
                end = max(end, intervals[j][1])
                j+=1

            output.append([start, end])
            i = j
        
        return output

        