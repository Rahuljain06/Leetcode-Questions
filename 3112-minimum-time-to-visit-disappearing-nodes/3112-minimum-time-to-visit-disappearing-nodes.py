class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        
        graph=defaultdict(list)
        ans=[-1]*n
        
        for u,v,t in edges:
            graph[u].append((t,v))
            graph[v].append((t,u))
        heap=[(0,0)]
        
        while heap:
            time,node=heapq.heappop(heap)
            if ans[node]!=-1:continue
            ans[node]=time
            
            for time2, newnode in graph[node]:
                time2+=time
                if time2<disappear[newnode]:
                    heapq.heappush(heap,(time2,newnode))
        return ans
            