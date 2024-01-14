class RecentCounter:

    def __init__(self):
        self.s=deque()
        
    def ping(self, t: int) -> int:
        self.s.append(t)
        i=0
        while i<len(self.s):
            if self.s[-1]-self.s[i]<=3000:
                return len(self.s)-i
            else:
                self.s.popleft()
            
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)