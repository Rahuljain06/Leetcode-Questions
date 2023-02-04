class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        a=[]
        b=[]
        for i,j in enumerate(s):
            if j==c:
                a.append(i)
        
        for i,j in enumerate(s):
            if j==c:
                b.append(0)
            else:
                mini=len(s)
                for x in a:
                    mini=min(mini,abs(x-i))
                b.append(mini)
        return b
                    
                    