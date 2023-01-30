class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        dp=[0]*(n+1)
        dp[1]=1
        for i in range(2,len(dp)):
            if i==2:
                dp[i]=dp[i-1]+dp[i-2]
            else:
                dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
        return dp[n]