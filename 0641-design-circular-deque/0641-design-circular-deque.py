class MyCircularDeque:

    def __init__(self, k: int):
        self.stack=[]
        self.k=k
    def insertFront(self, value: int) -> bool:
            if len(self.stack)<self.k:
                self.stack.insert(0,value)
                return True
            return False
        

    def insertLast(self, value: int) -> bool:
        if len(self.stack)<self.k:
            self.stack.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if self.stack:
            self.stack.pop(0)
            return True
        return False
        

    def deleteLast(self) -> bool:
        if self.stack:
            self.stack.pop()
            return True
        return False

    def getFront(self) -> int:
        
        return self.stack[0] if self.stack else -1

    def getRear(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return len(self.stack)==0

    def isFull(self) -> bool:
        return len(self.stack)==self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()