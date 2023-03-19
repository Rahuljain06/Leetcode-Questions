class Solution:
    def duplicateZeros(self, nums: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        zeros = nums.count(0)
        nlen = len(nums) + zeros
        
        i = len(nums) - 1
        j = nlen - 1
        while i!=j:
            if j < len(nums):
                nums[j] = nums[i]
            j-=1
            if nums[i] == 0:
                if j < len(nums): nums[j] = nums[i]
                j -= 1
            i-=1