class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        nums=set(arr)
        i=1
        while k>0:
            if i not in nums:
                k-=1
            i+=1
        return i-1
        
        