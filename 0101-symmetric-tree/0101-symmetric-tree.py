# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.valid(root.left,root.right)
    def valid(self,leftnode,rightnode):
        if leftnode is None or rightnode is None:
            return leftnode==rightnode
        
        if not(leftnode.val==rightnode.val):
            return False
        
        return self.valid(leftnode.left,rightnode.right) and self.valid(leftnode.right,rightnode.left)