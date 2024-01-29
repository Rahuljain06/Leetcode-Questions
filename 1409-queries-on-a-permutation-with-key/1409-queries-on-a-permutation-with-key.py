class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        nums=[i+1 for i in range(m)]
        res=[]
        for val in queries:
            res.append(nums.index(val))
            nums.remove(val)
            nums.insert(0,val)
        return res
            
        