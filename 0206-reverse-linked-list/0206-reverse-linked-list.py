# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        cur=head
        nxt=None
        while cur:
            nxt=cur.next
            cur.next=prev
            #ab ham dono pointer ko update kar denge
            prev=cur
            cur=nxt
        return prev
       
        