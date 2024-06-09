class Solution:
    def maxTotalReward(self, nums: List[int]) -> int:
        nums = list(set(nums))
        
        nums.sort()
        @cache
        def dp(i, cur):
            
            if i >= len(nums):
                return cur
        
            skip = dp(i+1, cur)
            if (nums[i] > cur):
                operation = dp(i+1, cur+nums[i])
            else:
                operation = skip
            return max(skip, operation)
        
        return dp(0, 0)
       
        