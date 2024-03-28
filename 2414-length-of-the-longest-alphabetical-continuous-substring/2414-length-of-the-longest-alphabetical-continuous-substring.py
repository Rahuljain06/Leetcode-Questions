class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        tr=1
        res=1
        for r in range(1,len(s)):
            if ord(s[r])==ord(s[r-1])+1:
                res+=1
            else:
                res=1
            tr=max(res,tr)
        return tr
                
            
            
            
                    
                