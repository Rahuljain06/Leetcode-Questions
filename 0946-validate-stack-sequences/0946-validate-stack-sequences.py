class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
#         time=O(n)
#         space=O(n)
#         stack=[]
#         i=0
#         for x in pushed:
#             stack.append(x)
            
#             while stack and stack[-1]==popped[i]:
                
#                 i+=1
#                 stack.pop()
                
#         return len(stack)==0

     # time=O(n)
      #space=O(1)
        i=0
        j=0
        for x in pushed:
            pushed[i]=x
            while i>=0 and pushed[i]==popped[j]:
                i,j=i-1,j+1
                
            i+=1
                    
        return i==0
        

            
        
        