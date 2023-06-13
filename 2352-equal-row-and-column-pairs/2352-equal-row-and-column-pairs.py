class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        hashMap = defaultdict(int)
        
        for row in grid:
            rowStr = tuple(row)
            hashMap[rowStr] += 1
        
        count = 0
        for j in range(n):
            col = [grid[i][j] for i in range(n)]
            colStr = tuple(col)
            count += hashMap[colStr]
        
        return count