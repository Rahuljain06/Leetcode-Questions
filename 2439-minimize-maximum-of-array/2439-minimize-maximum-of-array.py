class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        total=0
        res=0
        for i in range(len(nums)):
            total+=nums[i]
            res=max(res,math.ceil(total/(i+1)))
        return int(res)