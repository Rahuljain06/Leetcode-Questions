class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        nums.sort()
        c=0
        mod=10**9+7
        while i<=j:
            if nums[i]+nums[j]<=target:
                c+=(2**(j-i))%mod
                i+=1
            else:
                j-=1
        return c % mod
            
        
        