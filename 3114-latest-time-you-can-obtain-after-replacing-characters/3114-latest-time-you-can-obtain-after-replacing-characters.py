class Solution:
    def findLatestTime(self, s: str) -> str:
        s=list(s)
        if s[4]=="?":
            s[4]="9"
        if s[3]=="?":
            s[3]="5"
        if s[1]=="?" and s[0]!="1" and s[0]!="?" :
            s[1]="9"
        elif s[1]=="?":
            s[1]="1"
        if s[0]=="?" and (s[1]=="1" or s[1]=="0"):
            s[0]="1"
        elif s[0]=="?":
            s[0]="0"
        return "".join(s)
        
            