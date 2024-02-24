class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # basically ham pehle time ko key mankar ek dictionary banenge and uss ke andar jaakar har person ko map karenge uske baad ham sorted karke dictionary ke keys ko pata laga lenge ki iss time tak kitne logo ko secrets pata tha or kis kis ki meeting same time par ya uske baad hui hai or un logo ko secrets ke andar daalte jaayenge or last mai secrets return kar denge.
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
                if src in secrets: #secret tabhi failega agar kisi bhi person ko pata hoga uss prticular time par 
                    dfs(src, timemap[t])
            
        return list(secrets)