class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        #simple dijastrik hai     
        graph=defaultdict(list)
        ans=[-1]*n
        
        for u,v,t in edges:
            graph[u].append((t,v))
            graph[v].append((t,u))
            
        heap=[(0,0)]
        
        while heap:
            spendedtime,node=heapq.heappop(heap)
            if ans[node]!=-1:continue
            ans[node]=spendedtime
            
            for newtime, newnode in graph[node]:
                newtime+=spendedtime # isme hamne abhi tak spend kiya hua time + newtime ko add kar diya or agar vo disapper[node] ke time se kam hai tabhi ham uss node tak pahoch jayenge otherwise -1
                if newtime<disappear[newnode]:
                    heapq.heappush(heap,(newtime,newnode))
        return ans
            