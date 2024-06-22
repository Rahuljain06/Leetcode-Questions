class Solution:
    def numberOfSubarrays(self, A: List[int], k: int) -> int:
        def atMost(k):
            res = i = 0
            cnt=0
            for j in range(len(A)):
                cnt+= A[j] % 2!=0
                while cnt > k:
                    k += A[i] % 2
                    i += 1
                res += j - i + 1
            return res

        return atMost(k) - atMost(k - 1)

            