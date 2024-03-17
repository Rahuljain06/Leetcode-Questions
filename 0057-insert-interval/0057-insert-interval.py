class Solution:
    def insert(self, intervals: List[List[int]], n: List[int]) -> List[List[int]]:
        res= []
        for index, i in enumerate(intervals):
            if i[1] < n[0]:
                res.append(i)
            elif n[1] < i[0]:
                res.append(n)
                return res+intervals[index:]
            else:
                n[0] = min(n[0], i[0])
                n[1] = max(n[1], i[1])
        res.append(n)
        return res