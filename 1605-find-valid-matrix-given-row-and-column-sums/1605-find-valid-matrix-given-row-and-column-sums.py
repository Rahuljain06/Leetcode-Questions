class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        res=[[0]*len(colSum) for i in range(len(rowSum))]
        for i in range(len(res)):
            for j in range(len(res[0])):
                res[i][j]=min(rowSum[i],colSum[j])
                rowSum[i]-=res[i][j]
                colSum[j]-=res[i][j]
        return res
        