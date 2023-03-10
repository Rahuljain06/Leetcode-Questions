# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head):
        self.head = head
    def getRandom(self):  # cost O(n) Time
        ans = 0
        p, i = self.head, 0
        while p:
            if random.randint(0, i) == 0: # capacity of the reservoir is 1, because we just need to return a single num
                ans = p.val  # replace ans with i-th node.val with probability 1/i
            p = p.next
            i += 1
        return ans