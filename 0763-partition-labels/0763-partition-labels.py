class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d={}
        for i in range(len(s)):
            d[s[i]]=i
        size=0
        end=0
        a=[]
        for i in range(len(s)):
            size+=1
            end=max(end,d[s[i]])
            if i==end:
                a.append(size)
                size=0
        return a
            
            
            
        