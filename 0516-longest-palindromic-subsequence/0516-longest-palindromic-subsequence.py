class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        text2=s[::-1]
        text1=s
        dp=[[0]*(len(text2)+1) for i in range(len(text1)+1)]


        for i in range((len(dp))-2,-1,-1):
            for j in range(len(dp[0])-2,-1,-1):
                if text1[i]==text2[j]:
                    dp[i][j]=1+dp[i+1][j+1]
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j+1])
        return dp[0][0]