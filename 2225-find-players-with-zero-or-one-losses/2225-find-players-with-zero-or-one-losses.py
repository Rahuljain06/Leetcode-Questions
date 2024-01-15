from sortedcontainers import SortedDict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans=[[],[]]
        d=SortedDict()
        for i,j in matches:
            if i not in d:
                d[i]=1
            if j in d:
                d[j]-=1
            else:
                d[j]=0
        print(d)
        for i in d:
            if d[i]==1:
                ans[0].append(i)
            if d[i]==0:
                ans[1].append(i)
        return ans
        
            
                
                
        
        
