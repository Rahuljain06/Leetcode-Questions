class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s)==1 :
            return 1
        if len(set(s))==1:
            return 0
        l=0
        r=len(s)-1
        while l<r:
            if s[l]==s[r]:
                val=s[l]
                while s[l]==val:
                    l+=1
                while s[r]==val:
                    r-=1
                if l==r:
                    return 1
            else:
                return r-l+1
        return 0
                    