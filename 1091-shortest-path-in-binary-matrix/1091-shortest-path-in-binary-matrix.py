class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N=len(grid)
        nei=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        dq=deque([(1,0,0)]) if grid[0][0]==0 else deque()
        visited=set()
        
        while dq:
            dis,x,y=dq.popleft()
            if (x,y)==(N-1,N-1):
                return dis
            for dx,dy in nei:
                if 0<=x+dx<N and 0<=y+dy<N and grid[x+dx][y+dy]==0 and (x+dx,y+dy) not in visited:
                    visited.add((x+dx,y+dy))
                    dq.append((dis+1,x+dx,y+dy))
        return -1
        