class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum=0
        for i in range(len(mat)):
            sum+=mat[i][i]
        c=len(mat)-1
        i=0
        while c>=0:
            sum+=mat[i][c]
            c-=1
            i+=1
        if len(mat)%2!=0:
            return sum-mat[len(mat)//2][len(mat)//2]
        else:
            return sum
            
        
        