class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        [4,3,2,1]
        nums=set(nums)
        res=0
        for x in nums:
            if x-1 not in nums:
                y=x+1
                while y in nums:
                    y+=1
                res=max(res,y-x)
        return res