class Solution:
    def countStudents(self, A: List[int], B: List[int]) -> int:
        while A:
            if B[0] in A:
                A.remove(B[0])
                B.pop(0)
            else:
                break
        return len(B)