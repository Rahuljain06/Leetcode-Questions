class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix)==1:
            return matrix[0]
        res1=[]
        if len (matrix[0])==1:
            for i in range(len(matrix)):
                res1.append(matrix[i][0])
            return res1
                
        res=[]
        l=0
        r=len(matrix[0])
        t=0
        b=len(matrix)
        
        while l<r and t<b:
            for i in range(l,r):
                res.append(matrix[t][i])
            t+=1
            
            for i in range(t,b):
                res.append(matrix[i][r-1])
            r-=1
            print(l,r,t,b)
            if not (l<r and t<b):
                break
            
            for i in range(r-1,l-1,-1):
                res.append(matrix[b-1][i])
            b-=1
                
            for i in range(b-1,t-1,-1):
                res.append(matrix[i][l])
                
            l+=1
            
        return res