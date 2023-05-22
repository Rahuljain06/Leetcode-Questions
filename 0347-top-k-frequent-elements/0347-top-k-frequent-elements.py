class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==k:
            return nums
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        # reverse sorting on the basis of value and adding k keys in list
        a=sorted(d.items(), key=lambda x: x[1],reverse=True)
        res=[]
        i=0
        while k:
            res.append(a[i][0])
            i+=1
            k-=1
        return res
        