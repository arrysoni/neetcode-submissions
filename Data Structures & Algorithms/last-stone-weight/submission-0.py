import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max-heap via negation (heapq is min-heap only)
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            y = -heapq.heappop(heap)    # heaviest
            x = -heapq.heappop(heap)    # second heaviest
            if y != x:
                heapq.heappush(heap, -(y - x))  # leftover stone

        return -heap[0] if heap else 0