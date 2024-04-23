class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        num=Counter(nums)
        res=[]
        for i in range(len(nums)):
            if nums[i]-1 not in num and nums[i]+1 not in num and num[nums[i]]==1:
                res.append(nums[i])
        return res