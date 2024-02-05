class Solution:
    def firstUniqChar(self, s: str) -> int:
        x={}
      
        for i in s:
          if i in x:
            x[i]+=1
          else:
            x[i]=1
        for i in x:
          if x[i]==1:
            a=(s.index(i))
            return a
        return -1
