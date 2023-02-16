class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        result=[0,0]
        result[0]=self.findstartingindex(nums,target)
        result[1]=self.findendingindex(nums,target)
        return result
        
    def findstartingindex(self,nums,target):
        start=0
        end=len(nums)-1
        index=-1
        while start<=end:
            mid=start+(end-start)//2
            if nums[mid]==target:
                index=mid
                end=mid-1
            elif target<=nums[mid]:
                end=mid-1
            else:
                start=mid+1
        return index            

    def findendingindex(self,nums,target):
        start=0
        end=len(nums)-1
        index=-1
        while start<=end:

            mid=start+(end-start)//2
            if nums[mid]==target:
                index=mid
                start=mid+1
            elif target<=nums[mid]:
                end=mid-1
            else:
                start=mid+1
        return index
                
