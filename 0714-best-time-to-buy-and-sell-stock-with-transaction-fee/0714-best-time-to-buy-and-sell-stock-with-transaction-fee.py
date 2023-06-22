class Solution:
    def maxProfit(self, nums: List[int], fee: int) -> int:
        buy=-nums[0]
        sell=0
        for i in range(1,len(nums)):
            profit=nums[i]+buy-fee
            sell=max(sell,profit)
            buy=max(buy,sell-nums[i])
            print(buy,sell)
        return sell
            
            