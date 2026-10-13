import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # max-heap (store negatives)
        self.large = []  # min-heap

    def addNum(self, num: int) -> None:
        # Push into small, then move small's max into large
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Rebalance so small has >= as many elements as large
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0