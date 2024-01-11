class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # APPROACH: Ham Yaha 2 se start kar rhe hai loop kyunki hame minimum 3 length ki subarray chaiye to ham 2 index peeche jaakr check kar sake ki diff of curr index - prev index and diff of prev index- prev2 index agar equal ata hai to uski lenght alteast 3 hogi or ham apne dp me 1 append kar denge. ab problem hai tab 4 ki hogi to hame 2 add karna hoga 1 ki jgha [look at the first example] to ham dp[i-1]+1 karenge kyunki aar peechle index par koi bhi subarrray bani hogi to wha 1 hoga already to hame usme 1 or add kar denge for eg 1234 to 123 ka 1 and 1234 ka 2 or last me ham dp ka sum return na karna pade esiliye pehle h count me store kar lenge jisse ek iteration kam chale
        
        dp=[0]*len(nums)
        cnt=0
        for i in range(2,len(nums)):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                dp[i]=dp[i-1]+1
                cnt+=dp[i]
        return cnt