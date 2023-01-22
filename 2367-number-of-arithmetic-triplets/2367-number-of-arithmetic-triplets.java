class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        a=set(nums)
        for i in range(len(a)):
            if nums[i] + diff in a and nums[i] + 2 * diff in a:
                ans += 1
        
        return ans