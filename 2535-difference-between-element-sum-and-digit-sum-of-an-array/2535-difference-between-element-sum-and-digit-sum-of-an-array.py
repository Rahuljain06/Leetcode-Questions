class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        t=sum(nums)
        d=0
        for i in nums:
            while i:
                d+=i%10
                i//=10
        return (t-d)
                
                
            