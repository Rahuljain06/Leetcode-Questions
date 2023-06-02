class ListNode:
    
    def __init__(self,key,val,next=None):
        self.pair=[key,val]
        self.next=next
        
        
class MyHashMap:

    def __init__(self):
        self.s=1000
        self.h=[None]*self.s
        

    def put(self, key: int, value: int) -> None:
        idx=key%self.s
        if not self.h[idx]:
            self.h[idx]= ListNode(key,value)
            return
        else:
            cur=self.h[idx]
            prev=None
            while cur:
                if cur.pair[0]==key:
                    cur.pair[1]=value
                    return
                pre=cur
                cur=cur.next
            pre.next=ListNode(key,value)

    def get(self, key: int) -> int:
        idx=key%self.s
        cur= self.h[idx]
        while cur:
            if cur.pair[0]==key:
                return cur.pair[1]
            cur=cur.next
        return -1
    
    def remove(self, key: int) -> None:
        idx=key%self.s
        cur=self.h[idx]
        if cur is None:
            return 
        elif cur.pair[0]==key:
            self.h[idx]=cur.next
        else:
            pre=cur
            cur=cur.next
            while cur:
                if cur.pair[0]==key:
                    pre.next=cur.next
                    break
                pre=cur
                cur=cur.next
            
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
  # def __init__(self):
  #       self.data = [None] * 1000001
  #   def put(self, key: int, val: int) -> None:
  #       self.data[key] = val
  #   def get(self, key: int) -> int:
  #       val = self.data[key]
  #       return val if val != None else -1
  #   def remove(self, key: int) -> None:
  #       self.data[key] = None