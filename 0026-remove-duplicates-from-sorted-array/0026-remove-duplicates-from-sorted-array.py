class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        r = 1
        l =0
        while l<len(nums)-1:
            if(nums[l]!=nums[l+1]):
                nums[r] = nums[l+1]
                r+=1
            l+=1
        return r
            
        