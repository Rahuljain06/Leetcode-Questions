class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums=[i+1 for i in range(n)]
        i=0
        while len(nums)>1:
            i=(i+k-1)%len(nums)
            nums.pop(i)
        return nums[0]
                
                
                