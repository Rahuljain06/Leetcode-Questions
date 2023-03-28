class Solution:
    def threeSumClosest(self, num: List[int], target: int) -> int:
        num.sort()
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            l, r = i+1, len(num) - 1

            while l < r:
                sum = num[i] + num[l] + num[r]
                if sum == target:
                    return sum
                if abs(sum - target) < abs(result - target):
                    result = sum
                if sum < target:
                    l += 1
                elif sum > target:
                    r -= 1
        return result