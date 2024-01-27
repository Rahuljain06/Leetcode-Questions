# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        elif root.val>key:
            root.left=self.deleteNode(root.left,key)
        elif root.val<key:
            root.right=self.deleteNode(root.right,key)
        else:
            #pehle hamne check kiya ki root.left hai ya nhi agar nhi ho to directly root.right return kar diya [Trick: isme ye ho sakta hai root.right bhi na ho to None return ho jayega usse hame fark nhi padta]
            if not root.left:
                return root.right
            #fir hamne check kiya ki root.right hai ya nhi agar nhi ho to directly root.left return kar diya
            elif not root.right:
                return root.left
            else:
                #agar dono exist left and right to BST ki property maintain karne ke liye hame root ke right node me jaakr minimum dhoondna hoga and uss node ki val ko apne key node wali value se replace karna hoga & fir baad me uss node ko hatana hoga
                
                minNode=self.findmin(root.right)
                root.val=minNode.val
                root.right=self.deleteNode(root.right,minNode.val)
        return root
    
    def findmin(self,root):
        while root.left:
            root=root.left
        return root
            