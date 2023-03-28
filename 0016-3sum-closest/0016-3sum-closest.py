class Solution:
    def threeSumClosest(self, num: List[int], target: int) -> int:
        num.sort()
        result = float('inf')
        for i in range(len(num) - 2):
            l, r = i+1, len(num) - 1

            while l < r:
                sum = num[i] + num[l] + num[r]
                if abs(sum - target) < abs(result - target):
                    result = sum
                elif sum < target:
                    l += 1
                elif sum > target:
                    r -= 1
                else:
                    return sum
                    
        return result