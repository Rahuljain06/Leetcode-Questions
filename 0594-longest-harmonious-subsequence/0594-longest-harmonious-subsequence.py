class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        a=0
        for i in d:
            if i + 1 in d.keys():
                a = max(a, d[i] + d[i+1])
        return a