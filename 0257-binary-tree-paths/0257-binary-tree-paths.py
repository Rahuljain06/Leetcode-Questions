# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        l=[]
        def dfs(root,s):
            nonlocal l
            if root is None:
                return None
            s+=str(root.val) + "-" +">"
            if not root.left and not root.right:
                s=s[:-2]
                l.append(s)
            dfs(root.left,s)
            dfs(root.right,s)
        dfs(root,"")
        return l
        
        
        
        
        