# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

#         cur=list2
#         while cur.next:
#             cur=cur.next
            
#         nxt=None
#         cur1=list1
#         while cur1:
#             nxt=cur1.next
#             if a-1==0:
#                 cur1.next=list2
#                 cur1=nxt
#             a-=1
#             if b==0:
#                 cur1=nxt
#                 cur.next=nxt
#             b-=1
#             cur1=nxt
#         return list1


        cur=list2
        while cur.next:
            cur=cur.next
            
        cur1=list1
        while a-1!=0:
            cur1=cur1.next
            a-=1
            
        cur2=list1
        while b+1!=0:
            cur2=cur2.next
            b-=1
        
        cur1.next=list2
        cur.next=cur2
        return list1
    
        

 
                
                