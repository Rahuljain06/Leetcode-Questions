class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        if nums[0]>0 or nums[-1]<0 :
            return len(nums)
        
        s=0
        e=len(nums)-1
        neg=0
        pos=0
        while s<e:
            mid=(s+e)//2
            if nums[mid]<0:
                s=mid+1
            else:
                e=mid
        neg=e
        s=0
        e=len(nums)
        while s<e:
            mid=(s+e)//2
            if nums[mid]>0:
                e=mid
            else:
                s=mid+1
        pos=len(nums)-e
       
        return max(pos,neg)
            
            