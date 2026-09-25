class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            # Case 1: nums[mid] == target
            if (nums[mid] == target):
                return mid
            # Case 2: target is in the left sorted array
            if (nums[left] <= nums[mid]):

                if (nums[left] <= target < nums[mid]):
                    right = mid - 1
                else: 
                    left = mid + 1
            # Case 3: target is in the right sorted array
            else:
                if (nums[mid] < target <= nums[right]):
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1
            