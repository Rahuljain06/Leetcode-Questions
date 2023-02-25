class Solution:
    def mySqrt(self, x: int) -> int:
        # start=0
        # end=x
        # while start<=end:
        #     mid=start+(end-start)//2
        #     if mid*mid<=x<(mid+1)*(mid+1):
        #         return mid
        #     elif mid*mid>x:
        #         end=mid-1
        #     else:
        #         start=mid+1
        if x==0:
            return 0
        if x==1:
            return 1
        left, right = 1, x
        while left < right:
            mid = left + (right - left) // 2
            if mid * mid <= x:
                left = mid + 1
            else:
                right = mid
        return left -1
