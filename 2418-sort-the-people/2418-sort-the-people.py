class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        a=[]
        c=sorted(zip(heights,names),reverse=True)
        for i in c:
            a.append(i[1])
        return a