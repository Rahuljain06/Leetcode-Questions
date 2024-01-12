class Solution:
    @cache
    def numTrees(self, n: int) -> int:
        if n<=1:
            return 1
        res=0
        for i in range(n):
            #CATALAN NUMBER
            #C0C2+C1C1+C2C0 for N=3
            #C0C3+C1C2+C2C1+C3C0 for N=4
            res+=self.numTrees(i)*self.numTrees(n-i-1)
        return res