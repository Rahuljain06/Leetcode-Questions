class Solution:
    def countPoints(self, s: str) -> int:
        d={}
        for i in range(0,len(s),2):
            if s[i+1] in d:
                d[s[i+1]].add(s[i])
            else:
                d[s[i+1]]=set(s[i])
        cnt=0
        for i in d:
            if len(d[i])==3:
                cnt+=1
        return cnt
                
                
            
        