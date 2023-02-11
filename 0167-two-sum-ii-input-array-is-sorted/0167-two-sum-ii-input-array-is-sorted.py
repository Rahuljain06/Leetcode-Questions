class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i,j in enumerate(nums):
            if j in d:
                return [d[j]+1,i+1]
            else:
                d[target-j]=i
                
        