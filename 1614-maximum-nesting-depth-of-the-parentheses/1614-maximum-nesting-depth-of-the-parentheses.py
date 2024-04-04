class Solution:
    def maxDepth(self, s: str) -> int:
        cur=0
        res=0
        for i in s:
            if i=="(":
                cur+=1
                res=max(res,cur)
            elif i==")":
                cur-=1
        return res
            
            
                
        