class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        m = len(nums2)
        cnt = 0
        mapi = Counter(nums2)
        for i in range(n):
            if nums1[i] % k != 0:
                continue
            val = nums1[i] // k
            for j in range(1, isqrt(val) + 1):
                if val % j == 0:
                    cnt += mapi[j]
                    if j != val // j:
                         cnt += mapi[val // j]
        return cnt
        
        

                    