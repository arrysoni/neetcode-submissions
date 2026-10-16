import heapq
import math
from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # max-heap via negation
        heap = [-g for g in gifts]
        heapq.heapify(heap)

        for _ in range(k):
            biggest = -heapq.heappop(heap)           # richest pile
            heapq.heappush(heap, -math.isqrt(biggest))  # floor(sqrt) put back

        return -sum(heap)
