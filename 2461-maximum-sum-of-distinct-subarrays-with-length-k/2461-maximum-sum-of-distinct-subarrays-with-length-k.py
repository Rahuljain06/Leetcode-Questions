class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        d=defaultdict(int)
        res=0
        cur=0
        l=0
        for r in range(len(nums)):
            d[nums[r]]+=1
            cur+=nums[r]
            if len(d)==k:
                res=max(res,cur)
            if r>=k-1:
                d[nums[l]]-=1
                cur-=nums[l]
                if not d[nums[l]]:
                     del d[nums[l]]
                l+=1
        return res
                
                