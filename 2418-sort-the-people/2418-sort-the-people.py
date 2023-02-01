class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        #return [x[0] for x in sorted(zip(names,heights), key= lambda z: -z[1])]
        
        d={}
        for i,j in zip(names,heights):
            d[j]=i
        a=sorted(heights,key=lambda x:-x)
        c=[]
        for i in a:
            c.append(d[i])
        return c
       