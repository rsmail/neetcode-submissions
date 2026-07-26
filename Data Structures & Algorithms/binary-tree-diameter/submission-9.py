# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #plan: find bottom, have a global res var that tracks largest diameter of any given node
        res = 0
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            nonlocal res
            res = max(res, left + right)
            return 1 + max(left, right)
        dfs(root)
        return res


        