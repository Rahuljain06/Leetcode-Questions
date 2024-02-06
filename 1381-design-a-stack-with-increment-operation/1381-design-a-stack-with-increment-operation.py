class CustomStack:

    def __init__(self, maxSize: int):
        self.st=[]
        self.c=0
        self.mx=maxSize

    def push(self, x: int) -> None:
        if self.c<self.mx:
            self.st.append(x)
            self.c+=1
            

    def pop(self) -> int:
        if self.st:
            self.c-=1
            return self.st.pop()
        return -1

        

    def increment(self, k: int, val: int) -> None:
        a=[]
        while self.st:
            a.append(self.st.pop())
        while a:
            if k>0:
                self.st.append(val+a.pop())
            else:
                self.st.append(a.pop())
            k-=1
        
            


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)