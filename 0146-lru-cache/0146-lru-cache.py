class ListNode:
    
    def __init__(self,key,value):
        self.key=key
        self.val=value
        self.next=None
        self.prev=None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.d={}
        self.head=ListNode(0,0)
        self.tail=ListNode(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
        
    def get(self, key: int) -> int:
        if key in self.d:
            node=self.d[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.remove(self.d[key])
            
        elif self.capacity==len(self.d):
            self.remove(self.tail.prev)
            
        self.insert(ListNode(key,value))
        
    def remove(self,node):
        del self.d[node.key]
        node.prev.next=node.next
        node.next.prev=node.prev
        
    def insert(self,node):
        self.d[node.key]=node
        headnxt=self.head.next
        self.head.next=node
        node.prev=self.head
        headnxt.prev=node
        node.next=headnxt
        
        
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)