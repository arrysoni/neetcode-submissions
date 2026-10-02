class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)              # start with n, since indices only go to n-1
        for i, num in enumerate(nums):
            result ^= i ^ num           # XOR the index (0..n-1) and the value
        return result