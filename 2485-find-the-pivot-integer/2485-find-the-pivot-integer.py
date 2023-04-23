class Solution:
    def pivotInteger(self, n: int) -> int:
        lsum=n*(n+1)/2
        rsum=0
        for i in range(n,0,-1):
            rsum+=i
            if lsum==rsum:
                return i
            elif rsum>lsum:
                return -1
            lsum-=i
            
            