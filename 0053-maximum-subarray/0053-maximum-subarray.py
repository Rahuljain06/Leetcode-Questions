class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum=maxsum=nums[0]
        for i in nums[1:]:
            cursum=max(i,i+cursum)
            maxsum=max(maxsum,cursum)
        return maxsum   
        
