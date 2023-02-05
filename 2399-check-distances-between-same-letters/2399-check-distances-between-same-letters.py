class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d={}
        for i,j in enumerate(s):
            d[j]=d.get(j,[])+[i]
        for i in d:
            if d[i][1]-d[i][0]!=distance[ord(i)-ord("a")]+1:
                return False
        return True