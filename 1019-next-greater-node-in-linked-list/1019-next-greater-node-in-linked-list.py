# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans=[]
        st=[]
        curr=head
        idx=0
        while curr:
            ans.append(0)
            while st and st[-1][0]<curr.val:
                ans[st.pop()[1]]=curr.val
            st.append((curr.val, idx))
            curr=curr.next
            idx+=1
        return ans
        