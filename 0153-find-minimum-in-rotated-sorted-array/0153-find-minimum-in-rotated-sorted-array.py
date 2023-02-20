class Solution:
    def findMin(self, nums: List[int]) -> int:
        start=0
        last=len(nums)-1
        while start<last:
            mid=(start+last)//2
            if nums[mid]>nums[last]:
                start=mid+1
            else:
                last=mid
        return nums[start]