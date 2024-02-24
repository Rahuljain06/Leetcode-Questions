class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        secrets=set([0,firstPerson]) # person who knows secrets
        timemap={}
        
        for a,b,t in meetings:
            if t not in timemap:
                timemap[t]=defaultdict(list)
            timemap[t][a].append(b)
            timemap[t][b].append(a)

        def dfs(src,adj):
            if src in visited:
                return
            visited.add(src)
            secrets.add(src)
            for nei in adj[src]:
                dfs(nei,adj)
        
        for t in sorted(timemap.keys()):
            visited=set()
            for src in timemap[t]:
                if src in secrets: #secret tabhi failega agar kisi bhi src ko pata hoga
                    dfs(src, timemap[t])
            
        
        return list(secrets)