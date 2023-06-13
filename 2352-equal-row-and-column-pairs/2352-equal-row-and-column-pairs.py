class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        d = defaultdict(int)
        
        for row in grid:
            r = tuple(row)
            d[r]+=1
        
        cnt = 0
        for j in range(n):
            col = [grid[i][j] for i in range(n)]
            coltuple = tuple(col)
            cnt += d[coltuple]
        
        return cnt