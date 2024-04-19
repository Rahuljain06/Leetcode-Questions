class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def isPrime(n):
            if n==2:
                return True
            if n==1:
                return False
            for i in range(2,int(math.sqrt(n))+1):
                if n%i==0:
                    return False
            return True
        lidx=float("inf")
        ridx=float("inf")
        for i in range(len(nums)):
            if isPrime(nums[i]):
                lidx=i
                break
        for i in range(len(nums)-1,-1,-1):
            if isPrime(nums[i]):
                ridx=i
                break
        if lidx!=float("inf") and ridx!=float("inf"):
            return ridx-lidx
        