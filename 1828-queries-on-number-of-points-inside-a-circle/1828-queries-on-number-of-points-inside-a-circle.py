class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res=[]
        for x1,y1,r in queries:
            cnt=0
            for x2,y2 in points:
                if (x1-x2)**2 + (y1-y2)**2 <= r*r:
                    cnt+=1
            res.append(cnt)
        return res