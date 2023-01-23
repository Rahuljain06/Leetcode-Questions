class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[0]*(n-2) for _ in range(n-2)]
        for i in range(n - 2):
            for j in range(n - 2):
                maxi=0
                for k in range(0,3):
                    for l in range(0,3):
                        maxi = max(maxi,grid[k+i][l+j])
                res[i][j]=maxi
        return res
