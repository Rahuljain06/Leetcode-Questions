class Solution:
    def minimumLength(self, s: str) -> int:
        d=Counter(s)
        
        n=len(s)
        for i in d:
            res=(d[i]-1)//2
            if res>0:
                n-=res*2
        return n