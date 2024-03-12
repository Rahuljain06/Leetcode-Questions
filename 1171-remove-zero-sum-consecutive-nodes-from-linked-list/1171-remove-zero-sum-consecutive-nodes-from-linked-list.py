# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        d={0:dummy}
        pre=0
        curr=head
        while curr:
            pre+=curr.val
            d[pre]=curr
            curr=curr.next
        
        pre=0
        curr=dummy
        while curr:
            pre+=curr.val
            curr.next=d[pre].next
            curr=curr.next
        return dummy.next
        