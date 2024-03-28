class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        d=defaultdict(int)
        l=0
        maxi=0
        for r in range(len(nums)):
            d[nums[r]]+=1
            if d[nums[r]]>k:
                while nums[l]!=nums[r]:
                    d[nums[l]]-=1
                    l+=1
                l+=1
                d[nums[r]]-=1

            maxi=max(maxi,r-l+1)
        return maxi
            
            
                
                
                
            
            
            
            
        