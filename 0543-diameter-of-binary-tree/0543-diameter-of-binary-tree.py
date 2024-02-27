# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi=0
        
        def dfs(root):
            if not root:
                return 0
            lh=max(0,dfs(root.left))
            rh=max(0,dfs(root.right))
            nonlocal maxi
            maxi=max(maxi,lh+rh)
            return 1+max(lh,rh)
        dfs(root)
        
        return maxi
