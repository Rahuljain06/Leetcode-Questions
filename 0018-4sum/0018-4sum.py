class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                l, r = j + 1, len(nums) - 1
                while l < r:
                    remain = nums[i] + nums[j] + nums[l] + nums[r]
                    if remain > target:
                        r -= 1
                    elif remain< target: 
                        l += 1
                    else:
                        ans.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
        return ans