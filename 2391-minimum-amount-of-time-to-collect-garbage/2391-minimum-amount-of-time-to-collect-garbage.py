class Solution:
    def garbageCollection(self, nums: List[str], t: List[int]) -> int:
        res=len(nums[0])
        cnt=set()
        for i,val in enumerate(nums[1:][::-1]):
            for j in set(val):
                cnt.add(j)
            res+=len(val)+len(cnt)*t[-i-1]
        return res
            