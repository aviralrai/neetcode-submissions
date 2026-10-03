class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-1*num)
        heapq.heappush(self.large,-1*heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -1*heapq.heappop(self.large))

    def findMedian(self) -> float:
        s = len(self.small)
        l = len(self.large)
        if (s+l)%2 == 0:
            return ((-1*self.small[0])+self.large[0])/2
        else: return -1*self.small[0]
        