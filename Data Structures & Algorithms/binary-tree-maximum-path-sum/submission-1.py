# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):

            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # Excluding -ve nums: drop a child branch if its best path sum is negative
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            #Compute Path Sum w/ Split
            # This line also decides if a straight path or bent path is better!
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # Return best straight-down path from this node (no split) for the parent to extend
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]

