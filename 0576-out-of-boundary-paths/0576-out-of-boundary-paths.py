class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, sR: int, sC: int) -> int:
        @cache
        def dfs(r,c,move):
            ans=0
            if move<0:
                return 0
            if r<0 or r>=m or c<0 or c>=n:
                return 1
            ans+=dfs(r-1,c,move-1)
            ans+=dfs(r+1,c,move-1)
            ans+=dfs(r,c-1,move-1)
            ans+=dfs(r,c+1,move-1)
            return ans
        return dfs(sR,sC,maxMove)%1000000007
        
    
    
#     def solve(i, j, maxMove):
#             if maxMove < 0:
#                 return 0
#             if i < 0 or i >= m or j < 0 or j >= n:
#                 return 1
            
#             a = solve(i-1, j, maxMove - 1)
#             b = solve(i+1, j, maxMove - 1)
#             c = solve(i, j-1, maxMove - 1)
#             d = solve(i, j+1, maxMove - 1)
            
#             return a + b + c + d
        