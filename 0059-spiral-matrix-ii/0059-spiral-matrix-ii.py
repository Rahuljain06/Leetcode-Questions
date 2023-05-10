class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        l=0
        r=n
        t=0
        b=n
        val=0
        
        mat=[[0]*n for i in range(n)]
        while l<r and  t<b:
            for i in range(l,r):
                val+=1
                mat[t][i]=val
            t+=1
            
            
            for i in range(t,b):
                val+=1
                mat[i][r-1]=val
            r-=1
            
            
            for i in range(r-1,l-1,-1):
                val+=1
                mat[b-1][i]=val
            b-=1
                
            for i in range(b-1,t-1,-1):
                val+=1
                mat[i][l]=val
            l+=1
        return mat
                
                
                
        