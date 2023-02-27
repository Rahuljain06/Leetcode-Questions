class Solution:
    def findMin(self, nums: List[int]) -> int:
        start=0
        end=len(nums)-1
        
        while start<end:
            mid=start+(end-start)//2
            while(nums[mid]==nums[end] and mid != end):
                end-=1
            if nums[mid]>nums[end]:
                start=mid+1
            elif nums[mid]<nums[end]:
                end=mid
            
        return nums[start]
                