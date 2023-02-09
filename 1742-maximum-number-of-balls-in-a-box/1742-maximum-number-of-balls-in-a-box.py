class Solution:
    def countBalls(self, l: int, h: int) -> int:
        
        def a(n):
            sum=0
            while n:
                sum+=n%10
                n=n//10
            return sum
        
        d={}
        for i in range(l,h+1):
            n=a(i)
            if n in d:
                d[n]+=1
            else:
                d[n]=1
        return max(d.values())