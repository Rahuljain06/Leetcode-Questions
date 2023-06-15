# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return root 
        
        q=deque()
        q.append(root)
        mini=float("-inf")
        c=0
        d=0
        while q:
            su=0
            for i in range(len(q)):
                a=q.popleft()
                su+=a.val
                if a.left:
                    q.append(a.left)
                if a.right:
                    q.append(a.right)
            c+=1
            if mini<su:
                mini=su
                d=c
                
                
        return d
        