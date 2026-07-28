# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 1
        def dfs(root, most):
            if not root: return 0
            most = max(most, root.val)
            left = dfs(root.left, most)
            right = dfs(root.right, most)
            nonlocal res
            if root.left and root.left.val >= most:
                res += 1
            if root.right and root.right.val >= most:
                res += 1
        dfs(root, -sys.maxsize)
        return res
           
        