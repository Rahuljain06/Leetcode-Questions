class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d={}
        for i,j in items1:
            d[i]=d.get(i,0)+j
        for i,j in items2:
            d[i]=d.get(i,0)+j
        return sorted(d.items())
            