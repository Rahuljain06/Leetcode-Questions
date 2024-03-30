class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def subarrayWithKAtMost(nums,k):
            l=0
            res=0
            d=defaultdict(int)
            for r in range(len(nums)):
                d[nums[r]]+=1
                while len(d)>k:
                    d[nums[l]]-=1
                    if not d[nums[l]]:
                        del d[nums[l]]
                    l+=1
                res+=r-l+1
            return res
        return subarrayWithKAtMost(nums,k) - subarrayWithKAtMost(nums,k-1)

