class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        i=0
        
        n=len(s)
        cnt0=s.count("0")
        cnt1=0
        res=n-cnt0
        for i in range(n):
            if s[i]=="0":
                cnt0-=1
            elif s[i]=="1":
                res=min(res,cnt0+cnt1)
                cnt1+=1
        return res
            