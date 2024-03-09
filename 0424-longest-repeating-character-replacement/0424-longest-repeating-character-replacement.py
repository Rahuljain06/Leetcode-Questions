class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        l= 0
        res=0
        for r in range(len(s)):
            d[s[r]]=d.get(s[r],0)+1
            if (r-l+1 - max(d.values()))>k:
                d[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res
            