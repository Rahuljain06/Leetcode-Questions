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
        #ye hamne esiliye banaya ki jisse hame ek account baar baar visit na kare like kahi par aisa ho sakta hai ki mail repeated ho to iska matlab account same person ka hai and vo merge hona chaiye to vo pehle hi visit ho chuka hoga to jab last wala loop me and dfs me dobara se call nhi hoga
        visitedaccounts=[False]*len(accounts)
        for i,account in enumerate(accounts):
            for j in range(1,len(account)):
                d[account[j]].append(i)
        
        #to ham yaha par basically accounts list ke 0 value fir 1 value and so on...and emails jo common hai uska set bana rhe hai jisse ham repeated values add na kare... fir ham accounts[i] ke saare email par ek ek karke traverse kar rhe hai or emails set() me add kar rhe hai fir uss particular email kisi or index pe hai to jaise johnsmith@mail.com 0 and 1 par dono par hai to pehle emails me ham isse add kar denge fir dictionary se index check karenge jo ham pehle hi store kar liya hai..to hame waha se 1 milega fir ham 1 par dfs laga denge and uske saare email [emails set()] me add karenge neighours check karte hue and ye process chalta jayega..
        def dfs(i,emails):
            if visitedaccounts[i]:
                return
            visitedaccounts[i]=True
            
            for j in range(1,len(accounts[i])):
                email=accounts[i][j]
                emails.add(email)
                for nei in d[email]:
                    dfs(nei,emails)

        # ye hame esiliye call karna pada kyunki saare nodes connected nhi hai to ham har node par check karenge...
    
        for i,account in enumerate(accounts):
            if visitedaccounts[i]:
                continue
            name=account[0]
            emails=set()
            dfs(i,emails)
            res.append([name]+sorted(emails))
        return res
            
        
            
                            
                            