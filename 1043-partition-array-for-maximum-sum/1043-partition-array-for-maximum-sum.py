class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        # basically ham array ke ek ek karke sare elements par khade ho rhe  and waha se ham 3 steps aage dekh rhe hai or uss 3 elements ki s ub array me ham maximum store kar rhe hai jisko ham baad me window size se multiply kar rhe hai kyunki kisi-kisi case me window size 3 se kam hai.
        dp={}
        def dfs(i):
            if i>len(arr):
                return 0
            if i in dp:
                return dp[i]
            cur_max=0
            res=0
            for j in range(i,min(i+k,len(arr))):
                cur_max=max(cur_max,arr[j])
                window=j-i+1
                res=max(res,(cur_max*window + dfs(j+1)))
            dp[i]=res
            return res
        return dfs(0)
        