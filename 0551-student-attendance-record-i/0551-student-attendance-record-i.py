class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count("A")>=2:return False
        count=0
        for i in range(1,len(s)):
            if s[i]==s[i-1]=="L":
                count+=2
            else:
                count=0
            if count>=3:
                return False
        return True
            