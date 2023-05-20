# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        dummy=ListNode(next=head)
        curr=dummy
        while curr.next and curr.next.next:
            temp1=curr.next  # 1
            temp2=curr.next.next #2
            # swapping
            curr.next,temp1.next,temp2.next=temp2,temp2.next,temp1
            curr=temp1
        return dummy.next



