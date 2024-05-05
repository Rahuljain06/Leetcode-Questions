class Solution:
    def minAnagramLength(self, s: str) -> int:
        n=len(s)
        c=Counter(s)
        isV=False
        for i in range(1,n):
            if n%i==0:
                isV=True
                for a in c.values():
                    if a % (n//i)!=0:
                        isV=False
                        break
                if isV:
                    return i
        return n
                