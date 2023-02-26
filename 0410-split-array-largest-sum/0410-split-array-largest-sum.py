class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def feasible(capacity) -> bool:
            days = 1
            total = 0
            for num in nums:
                total += num
                if total > capacity:  # too heavy, wait for the next day
                    total = num
                    days += 1
                    if days > m:  # cannot ship within D days
                        return False
            return True

        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left