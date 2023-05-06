class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        nums.sort()
        c=0
        mod=10**9+7
        pows=[1]*len(nums)
        for i in range(1,len(nums)):
            pows[i]=(pows[i-1]*2)%mod
        i=0
        while i<=j:
            if nums[i]+nums[j]<=target:
                c+=pows[j-i]%mod
                i+=1
            else:
                j-=1
        return c % mod
            
        
        