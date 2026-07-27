# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        x = root.val
        res = 0
        def dfs(root, x):
            if not root:
                return None
            x = max(x, root.val)
            left = dfs(root.left, x)
            right = dfs(root.right, x)
            nonlocal res
            if root.val >= x:
                res += 1
            return res
        dfs(root, x)
        return res

        