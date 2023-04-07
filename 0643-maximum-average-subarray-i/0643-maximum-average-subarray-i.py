class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res=pre=sum(nums[:k])
        for i in range(1,len(nums)-k+1):
            pre+=nums[i+k-1]-nums[i-1]
            res=max(res,pre)
        return res/k
            
            
            
        res = prefs = sum(nums[:k])
        for i in range(len(nums)-k):
            prefs += (nums[i+k] - nums[i])
            res = max(res, prefs)
        return res/k