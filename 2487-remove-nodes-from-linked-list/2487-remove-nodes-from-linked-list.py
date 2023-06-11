# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = head
        st=[]
        while cur:
            while st and st[-1]<cur.val:
                st.pop()
            st.append(cur.val)
            cur=cur.next
        
        cur=None
        while st:
            cur=ListNode(st.pop(),cur)
        return cur
            
        