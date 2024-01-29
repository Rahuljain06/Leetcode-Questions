class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res=[]
        for i,j in zip(l,r):
            a=sorted(nums[i:j+1])
            diff=float("inf")
            for k in range(1,len(a)):
                if diff!=float("inf") and a[k]-a[k-1]!=diff:
                    res.append(False)
                    break
                else:
                    diff=a[k]-a[k-1]
            else:
                res.append(True)
        return res
                    
                
        