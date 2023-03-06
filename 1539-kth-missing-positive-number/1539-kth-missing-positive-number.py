class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        nums=set(arr)
        i=1
        while i<arr[-1] and k>0:
            if i not in nums:
                k-=1
            i+=1
        if k>0:
            return arr[-1]+k
        return i-1
        
        