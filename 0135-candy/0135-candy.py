class Solution:
    def candy(self, nums: List[int]) -> int:
        dpl=[1]*len(nums)
        dpr=[1]*len(nums)
        
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                dpl[i]=max(dpl[i],dpl[i-1])+1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]>nums[i+1]:
                dpr[i]=max(dpr[i],dpr[i+1])+1
        su=0
        for i in range(len(dpl)):
            su+=max(dpl[i],dpr[i])
            
        return su
        
        