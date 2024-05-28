class Solution:
    def checkRecord(self, s: str) -> bool:
        count=0
        countA=1 if s[0]=="A" else 0
        for i in range(1,len(s)):
            if s[i]==s[i-1]=="L":
                count+=2
            else:
                count=0
            if s[i]=="A":
                countA+=1
            if count>=3 or countA>=2:
                return False
        return True
            