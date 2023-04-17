class Solution:
    def kidsWithCandies(self, c: List[int], extra: int) -> List[bool]:
     
        a=max(c)
        for i in range(len(c)):
            
            if c[i]+extra>=a:
                c[i]=True
            else:
                c[i]=False
        return c
                
            
        