class Solution:
    def smallestString(self, s: str) -> str:
        s=list(s)
        flag=False
        for idx,i in enumerate(s):
            if s[idx]=="a" and flag:
                break
            if s[idx]!="a" :
                s[idx]=chr(ord(i)-1)
                flag=True
        if not flag:
            s[-1]="z"
        return "".join(s)
                
                
                