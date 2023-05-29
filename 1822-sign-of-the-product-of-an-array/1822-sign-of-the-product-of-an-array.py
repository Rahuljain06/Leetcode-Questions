class Solution:
    def arraySign(self, nums: List[int]) -> int:
        count=1
        for i in nums:
            if i==0:
                return 0
            elif i<0 and count ==-1:
                count=1
            elif i<0 and count ==1:
                count=-1
            
        return count