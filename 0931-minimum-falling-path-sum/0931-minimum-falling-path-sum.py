class Solution:
    
        #this problem will use DP 
#by taking the minimum value from itself plus one of the 3 values right above it

#EX: 
# 1  2  3   
# 4  5  6  
# 7  8  9 

# new value for number at A[1][1] will be  min(5 + 1, 5 + 2, 5 + 3)
# therefore it will be 5 + 1 = 6, and 6 will then replace the value at A[1][1]

#new value for number at A[1][0] will be  min(4 + 1, 4 + 2) = 5
#it will only have two values to compare since there is no upper left value

#new value for number at A[1][2] will be  min(6 + 2, 6 + 3) = 8
#it will only have two values to compare since there is no upper right value

    def minFallingPathSum(self, A: List[List[int]]) -> int:
        for i in range(1,len(A)):
            for j in range(len(A[0])):

                #edge cases are first column and last column which only have two paths from above
                if j == 0:
                    A[i][j]  = min((A[i][j] + A[i - 1][j]), (A[i][j] + A[i - 1][j + 1]) )

                elif (j == len(A[0]) - 1):
                    A[i][j]  = min((A[i][j] + A[i - 1][j]), (A[i][j] + A[i - 1][j - 1]) )

                #every other column will have three paths coming from above
                else:
                    A[i][j] = min(A[i][j] + A[i - 1][j],A[i][j] + A[i - 1][j + 1], A[i][j] + A[i - 1][j - 1])

        # Now that minimum falling sums for each value at the bottom row have been computer
        # We can just take the min of the bottow row to get the smallest overall path sum 
        return min(A[len(A) - 1])
    
    
#         def f(i,j,matrix,dp):

#             if j<0 or j>=len(matrix):
#                 return float("inf")

#             if dp[i][j]!=-1:
#                 return dp[i][j]
            
#             if i==0:
#                 return matrix[0][j]
            
            
#             s=matrix[i][j]+f(i-1,j,matrix,dp)
#             ld=matrix[i][j]+f(i-1,j-1,matrix,dp)
#             rd=matrix[i][j]+f(i-1,j+1,matrix,dp)
            
#             dp[i][j]=min(s,ld,rd)
            
#             return dp[i][j]
        
#         n=len(matrix)    
#         dp=[[-1]*n for i in range(len(matrix))]
#         mini=float("inf")
#         for j in range(len(matrix[0])):
#             mini= min(mini,f(n-1,j,matrix,dp))
#         return mini