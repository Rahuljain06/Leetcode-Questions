# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l=r=head
        curr=None
        while k-1>0:
            k-=1
            l=l.next
        curr=l
        while curr.next:
            curr=curr.next
            r=r.next
            
        l.val,r.val=r.val,l.val
        return head
        
            
            