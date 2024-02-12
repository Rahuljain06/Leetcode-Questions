class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        a=max(d.values())
        for i in nums:
            if d[i]==a:
                return i