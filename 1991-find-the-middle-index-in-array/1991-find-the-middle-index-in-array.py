class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        l=0
        r=sum(nums)
        for i,j in enumerate(nums):
            r-=j
            if l==r:
                return i
            l+=j
        return -1
        