class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        # if 1st column of row is 0 then we are flipping it
        for r in range(rows):
            if grid[r][0]==0:
                for c in range(cols):
                    grid[r][c]=0 if grid[r][c] else 1
        
        
        # flip cols
        
        for c in range(cols):
            cnt_one=0
            for r in range(rows):
                if grid[r][c]==1:
                    cnt_one+=1
            if cnt_one < rows-cnt_one:
                for r in range(rows):
                    grid[r][c]=0 if grid[r][c] else 1
        
        
        res=0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    res+=2**(cols-1-c)
        return res
                
                