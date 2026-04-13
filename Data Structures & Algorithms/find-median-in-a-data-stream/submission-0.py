class MedianFinder:

    def __init__(self):
        self.first_half = []
        self.second_half = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.first_half, -num)

        heapq.heappush(self.second_half, -heapq.heappop(self.first_half))

        if len(self.second_half) > len(self.first_half):
            heapq.heappush(self.first_half, -heapq.heappop(self.second_half))


    def findMedian(self) -> float:
        if len(self.first_half) == len(self.second_half):
            return (-self.first_half[0] + self.second_half[0]) / 2.0
        else:
            return -self.first_half[0]
        