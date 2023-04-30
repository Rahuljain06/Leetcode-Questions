class Solution:
    def isPerfectSquare(self, x: int) -> bool:
        start=0
        end=x
        while start<=end:
            mid=start+(end-start)//2
            if mid*mid==x:
                return True
            elif mid*mid>x:
                end=mid-1
            else:
                start=mid+1
        return False