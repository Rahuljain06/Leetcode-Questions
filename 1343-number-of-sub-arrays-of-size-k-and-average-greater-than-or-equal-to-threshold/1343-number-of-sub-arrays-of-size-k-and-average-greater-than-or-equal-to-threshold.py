class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, t: int) -> int:
        curr=0
        res=0
        l=0
        for r in range(len(nums)):
            curr+=nums[r]
            if r>=k-1:
                if curr/k>=t:
                    res+=1
                curr-=nums[l]
                l+=1
        return res
        
                