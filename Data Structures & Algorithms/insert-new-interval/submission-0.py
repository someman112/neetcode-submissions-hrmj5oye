class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx = 0
        output = []


        while idx < len(intervals) and intervals[idx][1] < newInterval[0]:
            output.append(intervals[idx])
            idx+=1
        
        start, end = newInterval[0], newInterval[1] 

        while idx < len(intervals) and intervals[idx][0] <= end:
            start = min(start, intervals[idx][0])
            end = max(end, intervals[idx][1])
            idx+=1

        
        output.append([start,end])

        while idx < len(intervals):
            output.append(intervals[idx])
            idx+=1
        
        return output
        