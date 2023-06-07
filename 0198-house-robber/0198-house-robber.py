class Solution:
    def rob(self, nums: List[int]) -> int:
#         rob1=0
#         rob2=0
        
#         for i in nums:
#             temp=max(rob1+i,rob2)
#             rob1=rob2
#             rob2=temp
#         return rob2


        # inc=nums[0]
        # exc=0
        # for i in range(1,len(nums)):
        #     ninc=exc+nums[i]
        #     nexc=max(inc,exc)
        #     inc=ninc
        #     exc=nexc
        # return max(inc,exc)
        
        
# ham isme  agar prev2 le rhe hai to current wali value nums[i] use kar rhe and ek doosre case me current nhi le rhe usme prev le rhe hai sirf and fir current me jo done me max aa rha hai save kar rhe hai and in the last me prev2=prev and prev=cur se update kar de rhe hai..
        prev2=0
        prev=nums[0]
        for i in range(1,len(nums)):
            take=nums[i]
            if i>1:
                take+=prev2
            nottake=0+prev
            
            cur=max(take,nottake)
            
            prev2=prev
            prev=cur
        return prev
        
        
            
        