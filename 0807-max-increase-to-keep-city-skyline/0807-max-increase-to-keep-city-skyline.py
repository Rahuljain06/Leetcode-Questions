class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rowmax=[0]*len(grid)
        colmax=[0]*len(grid)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                rowmax[r]=max(rowmax[r],grid[r][c])
                colmax[c]=max(colmax[c],grid[r][c])
        res=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                res+=min(rowmax[r],colmax[c])-grid[r][c]
        return res