class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums)!=1:
            i=1
            while i<len(nums):
                nums[i-1]=(nums[i-1]+nums[i])%10
                i+=1
            nums.pop()
        return nums[0]
            
            