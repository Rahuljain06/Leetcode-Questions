class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        dir=[[0,1],[0,-1],[1,0],[-1,0]]
        def bfs(r,c):
            q=deque()
            q.append((r,c))
            maxr,maxc=r,c
            while q:
                r,c=q.popleft()
                maxr=max(maxr,r)
                maxc=max(maxc,c)  
                for i,j in dir:
                    newr=r+i
                    newc=c+j
                    if newr>=0 and newr<len(land) and newc>=0 and newc<len(land[0]) and land[newr][newc]==1:
                        land[newr][newc]=0
                        q.append((newr,newc))
            return maxr,maxc
        res=[]
        for r in range(len(land)):
            for c in range(len(land[0])):
                if land[r][c]==1:
                    endr,endc=bfs(r,c)
                    res.append([r,c,endr,endc])
        return res