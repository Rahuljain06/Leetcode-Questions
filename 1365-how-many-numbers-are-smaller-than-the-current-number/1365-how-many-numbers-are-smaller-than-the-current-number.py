class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d={}
        nums1=sorted(nums)
        for i,j in enumerate(nums1):
            if j not in d:
                d[j]=i
        #{1:0 , 2:1, 3:3 , 8:4}
        
        for i,j in enumerate(nums):
            nums1[i]=d[j]
            
        return nums1
            
        
        