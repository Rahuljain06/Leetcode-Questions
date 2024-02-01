class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        i=1
        while len(nums)!=1:
            i=1
            a=[]
            while i<len(nums):
                a.append((nums[i-1]+nums[i])%10)
                i+=1
            nums=a
        return nums[0]
            
            