class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        #complexity O(n)
        total=0
        maxsum=float("-inf")
        cur_max=0
        minsum=float("inf")
        cur_min=0

        for i in range(len(nums)):
            total+=nums[i]
            
            #kadane algorithm to find max sum subarray
            cur_max+=nums[i]
            maxsum=max(cur_max,maxsum)
            if cur_max<0:
                cur_max=0
                
            # finding the min subset and subarray it from total to get max sum subarray  
            cur_min+=nums[i]
            minsum=min(minsum,cur_min)
            if cur_min>0:
                cur_min=0
        # if all the values are negative than we have the maximum of negatives
        if total==minsum:
            return maxsum
        return max(maxsum,total-minsum)
            
        
        
        
# ##This method has complexity O(n**2)
# class Solution:
#     def maxSubarraySumCircular(self, nums: List[int]) -> int:
#         maxi=float("-inf")
#         def helper(nums):
#             curr=0
#             for i in range(len(nums)):
#                 curr+=nums[i]
#                 nonlocal maxi
#                 maxi=max(curr,maxi)
#                 if curr<0:
#                     curr=0
#             return maxi
        
#         for i in range(len(nums)):
#             helper(nums[i:]+nums[:i])
#         return maxi
            