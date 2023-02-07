class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        res=0
        d={}
        for r,i in enumerate(fruits):
            if i in d:
                d[i]+=1
            else:
                d[i]=1
            while len(d)>2:
                d[fruits[l]]-=1
                if not d[fruits[l]]:
                    d.pop(fruits[l])
                l+=1
            res=max(res,r-l+1)
        return res