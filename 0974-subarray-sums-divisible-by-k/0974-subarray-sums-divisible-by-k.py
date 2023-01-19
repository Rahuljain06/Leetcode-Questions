class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d={0:1}
        cursum=0
        count=0
        for i in nums:
            cursum+=i
            rem=cursum%k
            if rem in d:
                count+=d[rem]
            d[rem]=d.get(rem,0)+1
        return count         
        