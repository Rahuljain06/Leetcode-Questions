class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        #APPROACH: Ham pehle to har index i ke liye ek hashmap bana denge  {{}, {}, {}} [Ham default dict esiliye use kar ehe jisse agar vo key hashmap me nhi ho to 0 return ho jaye] and har index i par count store karenge ki kitni aise subsequences hai jo i index par khatam hoti hai with a particular common differnce eg: {{1:2,2:1},{3:2,4:5}} [to isme 0 index par 1 difference ke 2 subsequece end hoti hai and 2 difference ki 1 end hoti hai] or fir ham baad me j index se i tak loop chalyenge or check karnege ki nums[i]-nums[j] ke diff ki koi subseuence already i index par hai agar hai to ham usk res me add kar denge or agr nhi hai 
        
        
        # use defaultdict(int) to easily get the difference in arithmetic subsequences ending with ```j```
        dp = [defaultdict(int) for _ in range(len(nums))]
        res = 0
        for i in range(len(nums)):
            for j in range(0,i):
                dif = nums[i]-nums[j]

                # Simply add it to the result.
                res += dp[j][dif]

                # Increase the number of elements in arithmetic subsequence at i with this dif.
                dp[i][dif] += dp[j][dif]+1
        return res