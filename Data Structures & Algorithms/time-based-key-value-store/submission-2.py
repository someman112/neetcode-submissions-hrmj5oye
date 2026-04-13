from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.d=defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if not self.d[key]:
            return ""
            
        start,end=0, len(self.d[key])-1

        while start<=end:
            mid = (start+end)//2

            if self.d[key][mid][1] <= timestamp:
                start=mid+1
            
            else:
                end=mid-1
        
        return self.d[key][end][0] if self.d[key][end][1] <= timestamp else ""
        
