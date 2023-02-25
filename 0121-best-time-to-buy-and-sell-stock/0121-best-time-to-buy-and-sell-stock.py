class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxprofit=0
        minprices=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<minprices:
                minprices=prices[i]
            maxprofit=max(maxprofit,prices[i]-minprices)
        
        return maxprofit
                