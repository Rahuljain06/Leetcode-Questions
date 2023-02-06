class Solution:
    def fairCandySwap(self, a: List[int], b: List[int]) -> List[int]:
        dif=(sum(a)-sum(b))//2
        a=set(a)
        for i in set(b):
            if i+dif in a:
                return [dif+i,i]