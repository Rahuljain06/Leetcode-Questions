class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        mini=-1
        i=0
        j=len(nums)-1
        while i<j:
            mini=max(mini,nums[i]+nums[j])
            i+=1
            j-=1
        return mini
            
            