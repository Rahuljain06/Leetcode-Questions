# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head.next
        prev=head
        sum=0
        while curr:
            if curr.val==0:
                prev=prev.next
                prev.val=sum
                sum=0
            sum+=curr.val
            curr=curr.next
        prev.next=None
        return head.next
                
                
                