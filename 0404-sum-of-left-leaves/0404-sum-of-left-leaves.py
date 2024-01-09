# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        s=0
        def dfs(root,isleft):
            nonlocal s
            if root is None:
                return None
            if not root.left and not root.right:
                s+=root.val if isleft else 0
            dfs(root.left, True)
            dfs(root.right, False)
        dfs(root, None)  
        return s
                