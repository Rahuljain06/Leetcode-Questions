class MyHashSet:

    def __init__(self):
        self.size=1000
        self.val=[None]*self.size
        
    def hash(self,key):
        return key%self.size
    
    def add(self, key: int) -> None:
        
        h=self.hash(key)
        if self.val[h]==None:
            self.val[h]=[key]
        elif key in self.val[h]:
            return
        else:
            self.val[h].append(key)
        
    def remove(self, key: int) -> None:
        
        h=self.hash(key)
        if self.val[h] is not None and key in self.val[h]:
            self.val[h].remove(key)
        
    def contains(self, key: int) -> bool:
        
        h=self.hash(key)
        if self.val[h] is not None and key in self.val[h]:
            return True
        return False
       
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)