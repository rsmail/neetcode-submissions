# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        res = 0
        def dfs(root, big):
            if not root:
                return 0
            nonlocal res
            if root.val >= big:
                res += 1
                big = root.val
            left = dfs(root.left, big)
            right = dfs(root.right, big)
        dfs(root, -sys.maxsize)
        return res