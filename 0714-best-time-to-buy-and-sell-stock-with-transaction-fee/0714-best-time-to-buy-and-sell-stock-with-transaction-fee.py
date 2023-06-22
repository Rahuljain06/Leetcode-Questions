class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
    
    

        n = len(prices)
        ans = 0
        minimum = prices[0]
        for i in range(1, n):
            if prices[i] < minimum:
                minimum = prices[i]
            elif prices[i] > minimum + fee:
                ans += prices[i] - fee - minimum
                minimum = prices[i] - fee
        return ans

    
    
            
            