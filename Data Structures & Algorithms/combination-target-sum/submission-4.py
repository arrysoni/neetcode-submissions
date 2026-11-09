class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return

            # choice 1: take nums[i] again (stay on i)
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()

            # choice 2: skip nums[i] for good
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res