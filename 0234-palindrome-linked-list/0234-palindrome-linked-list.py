# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # a=[]  time complexity is O(n) but space complexity is O(n)
        # while head:
        #     a.append(head.val)
        #     head=head.next
        # if a==a[::-1]:
        #     return True
        # return False
        
        #Space Complexity O(1) and time complexity O(n)
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
        prev=None
        nxt=None
        while slow:
            nxt=slow.next
            slow.next=prev
            prev=slow
            slow=nxt
            
            
        left,right=head,prev
        while right and left:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True
        