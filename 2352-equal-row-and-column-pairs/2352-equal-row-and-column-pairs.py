class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        d = {}
        
        for row in grid:
            r = tuple(row)
            d[r] = d.get(r,0)+1

        cnt = 0
        for j in range(n):
            col = [grid[i][j] for i in range(n)]
            c = tuple(col)
            cnt += d.get(c,0)
        
        return cnt