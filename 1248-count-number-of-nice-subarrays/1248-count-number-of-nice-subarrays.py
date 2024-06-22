class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(k):
            res = i = 0
            cnt=0
            for j in range(len(nums)):
                cnt+= nums[j] % 2!=0
                while cnt > k:
                    cnt-=nums[i]%2!=0
                    i += 1
                res += j - i + 1
            return res

        return atMost(k) - atMost(k - 1)

            