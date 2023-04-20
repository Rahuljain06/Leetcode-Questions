class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            while (nums[i]>0 and nums[i]<=n) and (nums[nums[i] - 1]!=nums[i]):
                c=nums[i]-1
                nums[i],nums[c]=nums[c],nums[i]
        
        
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1
            
            
        
        
# int n = nums.size(); 
#         for (int i = 0; i < n; i++)
#             while (nums[i] > 0 && nums[i] <= n && nums[nums[i] - 1] != nums[i])
#                 swap(nums[i], nums[nums[i] - 1]);
#         for (int i = 0; i < n; i++)
#             if (nums[i] != i + 1)
#                 return i + 1;
#         return n + 1;
#     }
# };