# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, least, most):
            if not root:
                return True
            if not (least < root.val < most):
                return False
            left = dfs(root.left, least, root.val)
            right = dfs(root.right, root.val, most)
            

            return left and right
        return dfs(root, -sys.maxsize, sys.maxsize)
        