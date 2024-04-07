class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        s=list(s)
        for idx,i in enumerate(s):
            dir=min(ord(i)-ord("a"),ord("z")-ord(i)+1)
            if k>=dir:
                k-=dir
                s[idx]="a"
            else:
                s[idx]=chr(ord(i)-k)
                break
        return "".join(s)
            
