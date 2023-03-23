class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low=0
        high=len(nums)-1
        def partition(nums,low,high):
            i=low-1
            pivot=nums[high]
            for j in range(low,high):
                if nums[j]<=pivot:
                    i+=1
                    nums[i],nums[j]=nums[j],nums[i]
            nums[i+1],nums[high]=nums[high],nums[i+1]
            
            return i+1
        def Quicksort(nums,low,high):
            if low<high:
            
                pi=partition(nums,low,high)
                
                Quicksort(nums,low,pi-1)
                Quicksort(nums,pi+1,high)
        Quicksort(nums,low,high)
            
            
        
        
            