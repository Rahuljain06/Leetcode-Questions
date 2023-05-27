class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        def smple_rob(nums):
            inc=nums[0]
            exc=0
            
            for i in range(1,len(nums)):
                inc,exc=exc+nums[i],max(inc,exc)
            return max(inc,exc)
        
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return nums[0]
        else:
            return max(smple_rob(nums[:-1]),smple_rob(nums[1:]))
            
            
            
            
            
            
        