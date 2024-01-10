# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # hamne count esiliye use kiya kyunki jab ham pathsum me iterate karenge to vo har baar 0 ho jayega to hame globally count chaiye tha to maine constructor par daal diya.
    def __init__(self):
        self.cnt=0
        self.dp={}
    
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        #cnt=0 # ye esiliye work nhi karega kyunki tab ham traverse kaege pathsum me o ye har baar 0 ho jayega or hame total nhi milega.
        #Approach: ham poore tree me traverse karenge or har node par dfs lagakar ye check karenge ki waha se koi bhi path aisa hai jiska sum target ke equal hai
        def dfs(node,target):
            if node is None:
                return 0
            if node.val==target:
                self.cnt+=1
            dfs(node.left, target-node.val)
            dfs(node.right, target-node.val)
        if root is None:
            return 0
        dfs(root,target)
        self.pathSum(root.left,target)
        self.pathSum(root.right,target)
        return self.cnt
        
        
        