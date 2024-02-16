class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c=Counter(arr)
        c=sorted(c.values())
        print(c)
        for i in range(len(c)):
            k-=c[i]
            if k<0:
                return len(c)-i
        return 0
            