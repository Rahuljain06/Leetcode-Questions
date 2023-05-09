class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        d={}
        if len(set(s)) != len(set(pattern)):
            return False
        if len(s) != len(pattern):
            return False
        for i,j in enumerate(pattern):
            if j in d and  d[j]!=s[i]:
                    return False
            else:
                d[j]=s[i]
        return True
                    
                
                
        