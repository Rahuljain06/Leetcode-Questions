class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        d=defaultdict(int)
        res=[0]*len(A)
        c=0
        for i in range(len(A)):
            d[A[i]]+=1
            if d[A[i]]==2:
                c+=1
            d[B[i]]+=1
            if d[B[i]]==2:
                c+=1
            res[i]=c
        return res
                