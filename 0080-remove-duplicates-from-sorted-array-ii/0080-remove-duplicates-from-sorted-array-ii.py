class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<3:
            return len(nums)
        j=2
        i=2
        while(i<len(nums)):
            if nums[i]!=nums[j-2]:
                nums[j] = nums[i]
                j+=1
            i+=1
        return j