class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap=[]
        for i in range(1,len(heights)):
            d=heights[i]-heights[i-1]
            if d>0:
                heapq.heappush(heap,d)
            if len(heap)>ladders:
                bricks-=heapq.heappop(heap)
            if bricks<0:
                return i-1
        return len(heights)-1
                
            
        