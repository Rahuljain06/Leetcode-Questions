class Solution:
    def maxIceCream(self, A: List[int], coins: int) -> int:
        A.sort()
        for i, a in enumerate(A):
            coins -= a
            if coins < 0:
                return i
        return len(A)