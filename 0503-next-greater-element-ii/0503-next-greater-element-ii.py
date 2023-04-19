class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        res = [-1] * len(nums)
        for i in range(len(nums)):
            while stack and (nums[stack[-1]] < nums[i]):
                res[stack.pop()] = nums[i]
            stack.append(i)
        for i in range(len(nums)):
            while stack and (nums[stack[-1]] < nums[i]):
                res[stack.pop()] = nums[i]
            
            
        return res
        
        
        
        # nums2 = nums * 2
        # d={}
        # st=[]
        # res=[]
        # for x in nums2:
        #     while st and st[-1]<x:
        #         a=st.pop()
        #         d[a]=d.get(a,[])+[x]
        #     st.append(x)
        # for i in nums:
        #     if i in d and len(d[i])>0:
        #         res.append(d[i][0])
        #         d[i].pop(0)
        #     else:
        #         res.append(-1)
        # return res
        
        
#         stack = []
#         res=[-1]*len(nums)
#         for i in range(len(nums)) * 2:
#             while stack and nums[stack[-1]] < nums[i]:
#                 res[stack.pop()] -= nums[i]
#             stack.append(i)
#         return res
    
        # stack, res = [], [-1] * len(A)
        #     for i in range(len(A)) * 2:
        #         while stack and (A[stack[-1]] < A[i]):
        #             res[stack.pop()] = A[i]
        #         stack.append(i)
        # return res