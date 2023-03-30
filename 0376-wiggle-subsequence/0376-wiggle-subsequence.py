class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length=1
        up=2
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1] and up!=True:
                length+=1
                up=True
            elif nums[i]<nums[i-1] and up!=False:
                length+=1
                up=False
        return length

        