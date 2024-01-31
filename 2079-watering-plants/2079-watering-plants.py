class Solution:
    def wateringPlants(self, nums: List[int], ca: int) -> int:
        res=0
        c=ca
        for i,val in enumerate(nums):
            if c>=val:
                c-=val
                res+=1
            else:
                c=ca-val
                res+=2*i+1
        return res
        