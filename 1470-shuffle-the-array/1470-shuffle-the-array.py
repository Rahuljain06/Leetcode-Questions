class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums3=[]
        for i in range(n):
            nums3.append(nums[i])
            nums3.append(nums[i+n])
        return nums3