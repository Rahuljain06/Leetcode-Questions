class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        #LIS jaisa bas len ki jgha array return karni hai
        
        nums.sort()
        dp=[[num] for num in nums]
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[j]%nums[i]==0 and len(dp[i]) < len(dp[j])+1:
                    dp[i]=[nums[i]]+dp[j]
        return max(dp,key=len)
    