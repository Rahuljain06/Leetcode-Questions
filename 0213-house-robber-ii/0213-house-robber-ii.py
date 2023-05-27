class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
#         def smple_rob(nums):
#             inc=nums[0]
#             exc=0
            
#             for i in range(1,len(nums)):
#                 inc,exc=exc+nums[i],max(inc,exc)
#             return max(inc,exc)
        
#         if len(nums)==0:
#             return 0
#         elif len(nums)==1:
#             return nums[0]
#         else:
#             return max(smple_rob(nums[:-1]),smple_rob(nums[1:]))
            
            
            # ham isme  agar prev2 le rhe hai to current wali value nums[i] use kar rhe and ek doosre case me current nhi le rhe usme prev le rhe hai sirf and fir current me jo done me max aa rha hai save kar rhe hai and in the last me prev2=prev and prev=cur se update kar de rhe hai..
        def logic(nums):
            prev2=0
            prev=nums[0]
            for i in range(1,len(nums)):
                take=nums[i]
                if i>1:
                    take+=prev2
                nottake=0 + prev

                cur=max(take,nottake)

                prev2=prev
                prev=cur
            return prev
        if len(nums)<2:
            return nums[0]
        
        return max(logic(nums[:-1]),logic(nums[1:]))
            
            
            
        