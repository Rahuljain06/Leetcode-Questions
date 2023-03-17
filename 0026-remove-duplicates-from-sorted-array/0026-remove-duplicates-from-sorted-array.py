class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 1
        i=0
        while i<len(nums)-1:
            if(nums[i]!=nums[i+1]):
                nums[x] = nums[i+1]
                x+=1
            i+=1
        return x
            
        