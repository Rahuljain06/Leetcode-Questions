class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d={}
        for i in range(len(order)):
            d[order[i]]=i
        
        res=[""]*len(d)
        for i in d:
            if i in s:
                res[d[i]]=i
        idx=0
        c=Counter(s)
        for i in d:   
            if i in d and c[i]>1:
                for _ in range(c[i]-1):
                    res.insert(d[i]+idx,i)
                    idx+=1
        for i in set(s):
            if i not in d:
                res+=[i]*c[i]
        return "".join(res)
                
                
        