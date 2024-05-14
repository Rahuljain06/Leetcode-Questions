class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        dir=[[0,-1],[-1,0],[1,0],[0,1]]
        
        def dfs(r,c):
            if r<0 or c<0 or r> rows-1 or c> cols-1 or grid[r][c]==0:
                return 0
            
            curr_one=grid[r][c]
            grid[r][c]=0
            ans=0
            for newr,newc in dir:
                ans=max(ans,dfs(r+newr,c+newc))
            grid[r][c]=curr_one
            return ans+curr_one
                
        maxi=0
        for r in range(rows):
            for c in range(cols):
                maxi=max(maxi,dfs(r,c))
        return maxi