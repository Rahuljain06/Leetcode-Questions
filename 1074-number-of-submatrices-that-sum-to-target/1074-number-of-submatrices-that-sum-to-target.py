class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])

        for x in range(m):
            for y in range(n - 1):
                matrix[x][y+1] += matrix[x][y]
        #print(matrix)
        res = 0
        for y1 in range(n):
            for y2 in range(y1, n):
        # d={0:1}
        # cursum=0
        # count=0
        # for i in nums:
        #     cursum+=i
        #     if cursum-k in d:
        #         count+=d[cursum-k]
        #     d[cursum]=d.get(cursum,0)+1
        # return count
                d = {0: 1}
                cursum = 0
                for x in range(m):
                    cursum += matrix[x][y2] - (matrix[x][y1-1] if y1 > 0 else 0)
                    if cursum-target in d:
                        res += d[cursum - target]
                    d[cursum] = d.get(cursum, 0) + 1
        return res
