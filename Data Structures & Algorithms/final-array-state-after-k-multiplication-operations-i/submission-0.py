import heapq
from typing import List

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(v, i) for i, v in enumerate(nums)]
        heapq.heapify(heap)

        for _ in range(k):
            val, idx = heapq.heappop(heap)
            val *= multiplier
            nums[idx] = val
            heapq.heappush(heap, (val, idx))

        return nums