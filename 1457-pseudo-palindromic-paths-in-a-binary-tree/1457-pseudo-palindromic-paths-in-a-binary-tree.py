# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        cnt=0
        def palindrome(d):
            nonlocal cnt
            miss=False
            for i in d:
                if d[i]%2!=0:
                    if miss:
                        return False
                    miss=True
            cnt+=1
        def dfs(root,res):
            nonlocal cnt
            if not root:
                return None
            res[root.val]+=1
            if not root.left and not root.right:
                if palindrome(res):
                    cnt+=1
            dfs(root.left,res)
            dfs(root.right,res)
            res[root.val]-=1
        dfs(root,defaultdict(int))
        
        return cnt
        
            
        