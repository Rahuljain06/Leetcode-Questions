class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        c=Counter(nums)
        res=0
        d=sorted(c,key=lambda x:(-x,c[x]))
        for i,val in enumerate(d[:-1]):
            res+=c[val]*(len(d)-i-1)
        return res
            
        
        