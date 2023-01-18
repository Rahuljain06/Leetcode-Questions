class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        t=0
        d=0
        for i in nums:
            t+=i
            while i:
                d+=i%10
                i//=10
        return t-d
                
                
            