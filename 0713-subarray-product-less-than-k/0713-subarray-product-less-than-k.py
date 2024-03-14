class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        total=1
        cnt=0
        while r<len(nums):
            total*=nums[r]
            while total>=k and l<=r:
                total//=nums[l]
                l+=1
            cnt+=r-l+1
            r+=1
        return cnt 
            