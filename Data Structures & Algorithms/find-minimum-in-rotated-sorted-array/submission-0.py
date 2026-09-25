class Solution:
    def findMin(self, nums: List[int]) -> int:

        min_num = nums[0]
        left = 0
        right = len(nums) - 1

        while left <= right:

            # Case 1: The list rotated to itself
            if (nums[left] < nums[right]):
                min_num = min(min_num, nums[left])
                break

            # Case 2: The list is randomly rotated
            mid = (left + right) // 2
            min_num = min(min_num, nums[mid])
            # The middle element is part of the left sorted list, min lies in right sorted list
            if (nums[left] <= nums[mid]):
                left = mid + 1
            else:
                right = mid - 1
        return min_num
        