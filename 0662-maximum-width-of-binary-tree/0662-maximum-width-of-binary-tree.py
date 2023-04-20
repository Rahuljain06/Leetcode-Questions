# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q=deque()
        q.append((root,0))
        res=0
        while q:
            start=q[0][1]
            end=q[-1][1]
            res=max(res,end-start+1)
            for i in range(len(q)):
                node=q.popleft()
                idx=node[1]-start # to avoid overflow condition evertytime we start our index with 0
                if node[0].left:
                    q.append((node[0].left,2*idx+1))
                if node[0].right:
                    q.append((node[0].right,2*idx+2))
        return res
            