# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a=None
        c=k
        b=None
        curr=head
        val=0
        while curr:
            k-=1
            if k==0:
                a=curr
            curr=curr.next
            val+=1
        print(val)
        curr=head
        while val-c>0 and curr:
            val-=1
            curr=curr.next
        b=curr
        a.val,b.val=b.val,a.val
        return head
            