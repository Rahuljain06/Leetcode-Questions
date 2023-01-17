class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        #on starting we ignore 0
        cnt0=0
        cnt1=0
        for i in range(len(s)):
            if s[i]=="1":
                cnt1+=1
            elif cnt1>=1 and s[i]=="0":
                cnt0+=1
            if cnt0>cnt1:
                cnt0=cnt1
        return cnt0
            