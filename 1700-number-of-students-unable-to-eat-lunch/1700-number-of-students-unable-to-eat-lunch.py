class Solution:
    def countStudents(self, A: List[int], B: List[int]) -> int:
        count = collections.Counter(A)
        n, k = len(A), 0
        while k < n and count[B[k]]:
            count[B[k]] -= 1
            k += 1
        return n - k