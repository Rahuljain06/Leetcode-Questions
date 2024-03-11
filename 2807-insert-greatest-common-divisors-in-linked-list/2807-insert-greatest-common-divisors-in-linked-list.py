# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=head
        cur=head.next
        
        while cur:
            val=math.gcd(prev.val,cur.val)
            gcdnode=ListNode(val)
            prev.next=gcdnode
            gcdnode.next=cur
            prev=cur
            cur=cur.next
        return head