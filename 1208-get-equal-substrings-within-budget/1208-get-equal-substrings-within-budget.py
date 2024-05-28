class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        maxi=0
        total=0
        l=0
        for r in range(len(s)):
            total+=abs(ord(t[r])-ord(s[r]))
            while total>maxCost:
                total-=abs(ord(t[l])-ord(s[l]))
                l+=1
            maxi=max(maxi,r-l+1)
        return maxi
        