# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

from typing import List


class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []
        arr = list(pairs)  # shallow copy of the list; Pair objects are shared, which is fine

        for i in range(len(arr)):
            j = i - 1
            curr = arr[i]

            # Strict ">" keeps equal keys in their original order (stable)
            while j >= 0 and arr[j].key > curr.key:
                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = curr
            res.append(list(arr))  # snapshot of the list, not a reference

        return res