class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])

        for x in range(m):
            for y in range(n - 1):
                matrix[x][y+1] += matrix[x][y]
        #print(matrix)
        
        # to ab ham basically ek column fix kar denge c1 and waha se c2 ko badenge or fir c2 ke andar jitni bhi rows hongi unka prefix sum wale tareeke se [560 question] se no . of matrices nikal lenge jo target ke equal hai. or fir aise karke poora matrix me har column par traverse karenge. matlab c1 ko badaenge i.e c1=1 or fir waha se c2 ko bada bada kar jitni bhi rows aayengi unka  prefix sum wale tareeke se [560 question] se no . of matrices nikal lenge or jab aage bada rhe hai to usse pehle jitni bhi columns hai usko subtract kar denge
        
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
