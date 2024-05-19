class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        preSum = [1]
        for i in range(1,len(nums)):
            if nums[i] % 2 == nums[i-1] % 2:
                preSum.append(preSum[-1])
            else:
                preSum.append(preSum[-1] + 1)
        res = []
        for s,e in queries:
            if preSum[e] - preSum[s] == e-s:
                res.append(True)
            else:
                res.append(False)
        return res