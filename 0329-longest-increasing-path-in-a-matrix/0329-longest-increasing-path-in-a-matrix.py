class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows=len(matrix)
        cols=len(matrix[0])
        #Approach: ham saare path me jaayenge or dictionary me har (r,c) par check karenge ki waha se kitna lamba path hai or last me jo max value store hogi usko return kar denge.

        d={}
        def dfs(r,c,prev): 
            if r<0 or c<0 or r>=rows or c>=cols or matrix[r][c]<=prev:
                return 0
            if (r,c) in d:
                return d[(r,c)]
            res=1
            res=max(res,1+dfs(r+1,c,matrix[r][c]))
            res=max(res,1+dfs(r-1,c,matrix[r][c]))
            res=max(res,1+dfs(r,c+1,matrix[r][c]))
            res=max(res,1+dfs(r,c-1,matrix[r][c]))
            d[(r,c)] = res
            return res
            
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,-1)
        return max(d.values())
        
        
        
        
        
        
        