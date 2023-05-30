class MyHashSet:

    def __init__(self):
        self.val=[False]*(1000000+1)
        

    def add(self, key: int) -> None:
        self.val[key]=True
        

    def remove(self, key: int) -> None:
        self.val[key]=False
        

    def contains(self, key: int) -> bool:
        return self.val[key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)