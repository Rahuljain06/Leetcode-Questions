class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        a=[0]*26
        b=[]
        for i in range(len(p)):
            a[ord(p[i])-ord("a")]+=1
            a[ord(s[i])-ord("a")]-=1
        if a==[0]*26:
            b.append(0)
        for i in range(len(p),len(s)):
            a[ord(s[i])-ord("a")]-=1
            a[ord(s[i-len(p)])-ord("a")]+=1
            if a==[0]*26:
                b.append(i-len(p)+1)
        return b