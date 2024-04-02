class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        c=Counter(nums)
        res=0
        d=sorted(c,reverse=True)
        for i,val in enumerate(d):
            res+=c[val]*(len(d)-i-1)
        return res
            
        
        