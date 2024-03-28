class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        t=1
        tr=1
        for r in range(1,len(prices)):
            if prices[r]+1==prices[r-1]:
                t+=1
                tr+=t
            else:
                t=1
                tr+=1
        return tr
            
            
            