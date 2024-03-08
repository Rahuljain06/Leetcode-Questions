class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d={}
        maxi=1
        for i in nums:
            if i in d:
                d[i]+=1
                maxi=max(maxi,d[i])
            else:
                d[i]=1
        cnt=0
        for i in d:
            if d[i] ==maxi:
                cnt+=maxi
        return cnt
                