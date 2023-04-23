class Solution:
    def pivotInteger(self, n: int) -> int:
        rsum=n*(n+1)/2
        csum=0
        for i in range(n,0,-1):
            csum+=i
            if rsum==csum:
                return i
            elif csum>rsum:
                return -1
            rsum-=i
            
            