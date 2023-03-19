class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums=sorted(nums)
        k -= 1
        mini = float('inf')
        for i in range(len(nums)-k):
            mini = min(mini, nums[i+k]-nums[i])
        
        return mini