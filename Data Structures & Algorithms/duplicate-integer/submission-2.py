class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if len(nums) == 0 or len(nums) == 1:
            return False

        dic = {}
        for i in range(len(nums)):

            dic[nums[i]] = dic.get(nums[i], 0) + 1
            if dic[nums[i]] > 1:
                return True
        return False
