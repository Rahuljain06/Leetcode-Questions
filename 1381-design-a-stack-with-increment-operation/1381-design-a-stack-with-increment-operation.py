class CustomStack:

    def __init__(self, maxSize: int):
        self.st=[]
        self.c=0
        self.mx=maxSize

    def push(self, x: int) -> None:
        if self.mx:
            self.st.append(x)
            self.mx-=1
            

    def pop(self) -> int:
        if self.st:
            self.mx+=1
            return self.st.pop()
        return -1

        

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.st))):
            self.st[i] += val
        
            


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)