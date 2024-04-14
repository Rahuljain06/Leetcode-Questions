class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        
        points=[i[0] for i in points]
        points=sorted(list(set(points)))
        if len(points)==1:
            return 1
        print(points)
        res=0
        l=0
        for r in range(1,len(points)):
            if points[r]-points[l]>w:
                l=r
                res+=1
        if l<=r:
            res+=1
        return res

                
        