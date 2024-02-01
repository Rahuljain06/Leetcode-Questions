class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        s=set(nums)
        for i in nums:
            a=str(i)[::-1]
            s.add(int(a))
        return len(s)
            
            