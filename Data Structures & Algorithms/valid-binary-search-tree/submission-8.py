# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, small, large):
            if not root:
                return True
            if not (small < root.val < large):
                return False
            left = dfs(root.left, small, root.val)  
            right = dfs(root.right, root.val, large)
            return left and right
        return dfs(root, -sys.maxsize, sys.maxsize)
        