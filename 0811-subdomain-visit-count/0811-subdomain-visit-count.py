class Solution:
    def subdomainVisits(self, nums: List[str]) -> List[str]:
        d=defaultdict(int)
        
        for i in nums:
            i=i.split(" ")
            a=i[1]
            a=a.split(".")
            for j in range(len(a)):
                k=".".join(a[j:])
                d[k]+=int(i[0])
        res=[]
        for i in d:
            val=str(d[i])+" " + i
            res.append(val)
        return res
            
            