class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)==1:return True
        f= 1 if nums[0]%2==0 else -1
        for i in range(1,len(nums)):
            if nums[i]%2==0 and f==1:
                return False
            elif nums[i]%2 !=0 and f==-1:
                return False
            f*=-1
        return True
                
        