class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        free_servers=[i for i in range(k)]
        used_servers=[] #[end, server]
        count_server =[0]*k
        
        for i,start in enumerate(arrival):
            while used_servers and used_servers[0][0]<=start:
                _, server= heappop(used_servers)
                heappush(free_servers, i+(server-i)%k)
            if free_servers:
                server = heappop(free_servers) % k
                heappush(used_servers, (start+load[i],server))
                count_server[server]+=1
        max_value=max(count_server)
        res=[]
        for i,val in enumerate(count_server):
            if val==max_value:
                res.append(i)
        return res