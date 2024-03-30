class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        sum = 0
        d = 0
        b = 0
        for i in range(len(possible)):
            if possible[i] == 1:
                sum += 1
            else:
                sum -= 1
        for i in range(len(possible) - 1):
            if possible[i] == 1:
                d += 1
            else:
                d -= 1
            b = sum - d
            if d > b:
                return i + 1
        return -1