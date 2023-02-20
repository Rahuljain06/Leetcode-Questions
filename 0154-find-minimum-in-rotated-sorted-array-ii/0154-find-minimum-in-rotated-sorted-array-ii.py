class Solution:
    def findMin(self, nums: List[int]) -> int:
        start=0
        end=len(nums)-1
        
        while start<end:
            mid=start+(end-start)//2
            if nums[mid]>nums[end]:
                start=mid+1
            elif nums[mid]<nums[end]:
                end=mid
            else:
                end-=1
        return nums[start]
                