class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        l=0
        maxi=0
        total=0
        nums.sort()
        for r in range(len(nums)):
            total+=nums[r]
            while total+k < nums[r]*(r-l+1):
                total-=nums[l]
                l+=1
            maxi=max(maxi,r-l+1)
        return maxi
                
            