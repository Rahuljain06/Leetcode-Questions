class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        cur=0
        maxi=max(nums)
        l=0
        res=0
        for r in range(len(nums)):
            cur+=1 if nums[r]==maxi else 0
            while cur==k:
                if nums[l]==maxi:
                    cur-=1
                l+=1
            res+=l
        return res
            
            
            
        