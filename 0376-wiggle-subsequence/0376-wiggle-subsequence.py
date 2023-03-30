class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length=1
        up=2
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1] and up!=1:
                length+=1
                up=1
            elif nums[i]<nums[i-1] and up!=0:
                length+=1
                up=0
        return length

        