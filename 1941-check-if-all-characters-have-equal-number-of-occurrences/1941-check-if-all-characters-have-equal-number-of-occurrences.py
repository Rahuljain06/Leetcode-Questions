class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d=collections.Counter(s)
        a=d[s[0]]
        for i,j in enumerate(d,1):
            if d[j]!=a:
                return False
        return True
            
        
        