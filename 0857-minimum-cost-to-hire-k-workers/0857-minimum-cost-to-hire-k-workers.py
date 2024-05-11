class Solution:
    def mincostToHireWorkers(self,quality, wage, K):
        # hame basically k workers equal pay karna hai and vo wage/quality se nikal lenge. ye bilkul waise hi ki per hr kitna pay karna hai.. to hame ye vlue minimize karni hai to uske liye ham pehle ratio nikalkar sort kar lenge jisse hame  fir usme se k peoples select karenge and fir 
        workers=[]
        for w, q in zip(wage, quality):
            workers.append((w/q, w, q))
        workers.sort()
        cost= float('inf')
        team=[]
        totalq=0
        for ratio, w, q in workers:
            heapq.heappush(team, -q)
            totalq+= q
            if len(team) > K:
                totalq += heapq.heappop(team) # ham yaha par add esiliye kar rhe hai kyuni hamne values -ve me daali hai kyunki ye maxheap hai
            if len(team) == K:
                cost = min(cost, totalq * ratio)   
        return cost