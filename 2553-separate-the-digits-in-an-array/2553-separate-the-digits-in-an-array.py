class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:  
        res = []
        for i in range(len(nums)-1,-1,-1):
            num = nums[i]
            while num :
                res.append(num%10)
                num = num //10
        return res[::-1]