class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        n = len(nums)
        pos, neg, res = 0, 0, 0

        for i in range(n):
            d=target[i] - nums[i]

            if d>0:
                if pos<d:
                    res+=d-pos
                pos=d
                neg=0
            elif d < 0:
                if neg < -d:
                    res+=-d-neg
                neg=-d
                pos=0
            else:
                pos=0
                neg=0
        return res
       