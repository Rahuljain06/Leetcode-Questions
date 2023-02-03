class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s)<numRows or numRows==1:
            return s
        a= [""]*numRows
        
        par=0
        d=1
        
        for i in s:
            a[par]+=i
            if par==0:
                d=1
            if par==numRows-1:
                d=-1
            par+=1*d
        return "".join(a)