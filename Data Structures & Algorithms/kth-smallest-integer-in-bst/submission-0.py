# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ls = []
        def dfs(root):
            if not root:
                return None
            

            nonlocal ls
            ls.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        ls = sorted(ls)
        return ls[k - 1]

        

        