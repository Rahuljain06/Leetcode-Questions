# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
#         BFS
#         q=collections.deque()
#         q.append((root,1))
#         while q:
#             node,depth=q.popleft()
#             if not node.left and not node.right:
#                 return depth
#             if node.left:
#                 q.append((node.left,depth+1))
#                 print(q)
#             if node.right:
#                 q.append((node.right,depth+1))
#                 print("A",q)
        #DFS
        if not root.left and not root.right:
            return 1
        if  root.right and not root.left:
            return 1+self.minDepth(root.right)
        if root.left and not root.right:
            return 1+self.minDepth(root.left)
        return 1+min(self.minDepth(root.left),self.minDepth(root.right))