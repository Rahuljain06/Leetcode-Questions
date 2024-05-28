class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        pre=[abs(ord(t[0])-ord(s[0]))]
        for i in range(1,len(s)):
            pre.append(abs(ord(t[i])-ord(s[i])))
        maxi=0
        total=0
        l=0
        for r in range(len(pre)):
            total+=pre[r]
            while total>maxCost:
                total-=pre[l]
                l+=1
            maxi=max(maxi,r-l+1)
        return maxi
        