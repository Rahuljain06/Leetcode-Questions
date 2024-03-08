class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        #ham emails ko account se map kar rhe hai
        # johnsmith@mail.com : 0,1
        # john_newyork@mail.com: 0
        # john00@mail.com:1
        # mary@mail.com: 2
        # johnnybravo@mail.com: 3
        d=defaultdict(list)
        res=[]
        visitedaccounts=[False]*len(accounts)
        for i,account in enumerate(accounts):
            for j in range(1,len(account)):
                d[account[j]].append(i)
        
        
        
        def dfs(i,emails):
            if visitedaccounts[i]:
                return
            visitedaccounts[i]=True
            
            for j in range(1,len(accounts[i])):
                email=accounts[i][j]
                emails.add(email)
                for nei in d[email]:
                    dfs(nei,emails)
    
        for i,account in enumerate(accounts):
            if visitedaccounts[i]:
                continue
            name=account[0]
            emails=set()
            dfs(i,emails)
            res.append([name]+sorted(emails))
        return res
            
        
            
                            
                            