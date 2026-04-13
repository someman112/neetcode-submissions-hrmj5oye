class TimeMap:

    def __init__(self):
        self.data = {}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key in self.data:
            self.data[key].append((timestamp, value))
        else:
            self.data[key] = [(timestamp, value)]


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        lst = self.data[key]
        l,r = 0,len(lst)-1

        while l<r:
            mid = r - (r - l) // 2

            if lst[mid][0] > timestamp:
                r = mid - 1
            else:
                l = mid
        

        if lst[r][0] > timestamp:
            return ""

        return lst[r][1]