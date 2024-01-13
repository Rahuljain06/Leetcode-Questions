# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        #preorder=root, left, right
        #postorder=left,right, root
        #iss question me hame ye pata hai ki preorder[0] bhi root hai and postorder[-1] bhi root hai to ab ham ye jaante ki postorder me root se ek pehle value right hoti hai to ham right value dhoondenge preorder me konse index par hai fir jis index par bhi milegi to isse pehle wali value left me [0 value ki exclude karke kyunki preorder me vo root hoti hai] or iski baad wali value right par pass kar denge and postorderlke left me jo index aayega usme se 0 :index-2[included] kyunki hame preorder ke lef me agar 3 value pass hui to postorder  me bhi 3 hi value pass hogi to uss hisab se ham preorder me pehla index use hi kar sakte to esiliye postorder left ki conditon 0:index-2[included] tak hi value pass hogi or right me index-1:-2[inc] kyunki potorder[-1] root tha
        if not preorder or not postorder: 
            return None
        root=TreeNode(preorder[0])
        if len(postorder)==1:
            return root
        mid=preorder.index(postorder[-2])
        root.left=self.constructFromPrePost(preorder[1:mid],postorder[:mid-1])
        root.right=self.constructFromPrePost(preorder[mid:],postorder[mid-1:-1])
        return root
        