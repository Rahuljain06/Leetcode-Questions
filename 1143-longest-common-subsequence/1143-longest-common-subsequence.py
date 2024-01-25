class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        dp={}
        def backtrack(i,j):
            if i==len(s1) or j ==len(s2):
                return 0
            elif (i,j) in dp:
                return dp[(i,j)]
            elif s1[i]==s2[j]:
                dp[(i,j)]= 1+backtrack(i+1,j+1)
            elif s1[i]!=s2[j]:
                dp[(i,j)]=max(backtrack(i+1,j),backtrack(i,j+1))
            return dp[(i,j)]
        return backtrack(0,0)
    
    
#     dp=[[0]*(len(text2)+1) for i in range(len(text1)+1)]
        
        
#         for i in range((len(dp))-2,-1,-1):
#             for j in range(len(dp[0])-2,-1,-1):
#                 if text1[i]==text2[j]:
#                     dp[i][j]=1+dp[i+1][j+1]
#                 else:
#                     dp[i][j]=max(dp[i+1][j],dp[i][j+1])
#         return dp[0][0]
    