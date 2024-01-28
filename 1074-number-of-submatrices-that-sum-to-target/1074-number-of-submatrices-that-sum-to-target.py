class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])

        for x in range(m):
            for y in range(n - 1):
                matrix[x][y+1] += matrix[x][y]
        #print(matrix)
        res = 0
        for c1 in range(n):
            for c2 in range(c1, n):
                d = {0: 1}
                cursum = 0
                for r in range(m):
                    cursum += matrix[r][c2] - (matrix[r][c1-1] if c1 > 0 else 0)
                    if cursum-target in d:
                        res += d[cursum - target]
                    d[cursum] = d.get(cursum, 0) + 1
        return res
