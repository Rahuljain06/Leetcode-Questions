class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d=[0]*26
        for i in s:
            d[ord(i)-ord("a")]+=1
        for j in t:
            if d[ord(j)-ord("a")]>=1:
                d[ord(j)-ord("a")]-=1
        return sum(d)
        
            
        