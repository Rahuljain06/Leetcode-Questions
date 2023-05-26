# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        tmp=head #4
        cnt=0
        while tmp and cnt<k:
            tmp=tmp.next
            cnt+=1
        
        if cnt<k:
            return head 
    
        prev=None
        cur=head
        dummy=head
        nxt=None
        
        for i in range(k):
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        dummy.next=self.reverseKGroup(cur,k)#4,3
        return prev