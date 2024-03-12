# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #isme hamne har ek point pa prefixsum store kar liya hai hashmap mai [Subarray Sum Equals K ki tarah] fir jab bhi same sum repeat ho rha hai ham uss point ke node ko replace kar de rhe hai for eg: [1,2,3,-3,-2] iss array ki prefix sum ka hashmap kuch aise banega [1:-2,3:-3,6:3] # [sum:node] =>[ [1:0,3:1,6:2,3:3,1:4] to ham isme jo repeated sum aya usko overwrite kar denge to ye [1:4,3:3,6:2] #[sum:idx] aisa banega map] fir ham dobara se loop chalakar ham prefix sum nikalenge or prefix sum map  me jo node save hoga uske prefix sum ke corresponing uski next value ko point kar denge [next value par point esiliya kiya kyunki hame vo value bhi nahi chaiye eg: [1:-2,3:-3,6:3] to isme first index me hamne -2 save kiya to iska matlab hame -2 node ka next value chaiye kyunki [1,2,3,-3,-2] ka ans [1] hoga to hame -2 bhi remove karna hai] 
        
        dummy=ListNode(0)
        dummy.next=head
        d={0:dummy} #[sum:node]
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
        