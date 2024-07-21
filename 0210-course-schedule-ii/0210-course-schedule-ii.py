class Solution:
    def findOrder(self, nums: int, prerequisites: List[List[int]]) -> List[int]:
        # we need to have PreMap to map the preRequisites
        
        preMap={i:[] for i in range(nums)}
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
            
        op=[]
        
        # now we are going to write dfs to visit preRequisites
        
        noCycle=set()
        checkCycle=set()
        
        def dfs(crs):
            
            if crs in checkCycle: return False
    
            if crs in noCycle:  return True
            
            checkCycle.add(crs)
            noCycle.add(crs)
            for pre in preMap[crs]:
                
                if not dfs(pre): return False     # if we detect cycle we will directly return False

            checkCycle.remove(crs) # After visiting all its PreRequsites, we find out there is no cycle present in the current crs and now we can remove it from visted. So, if this course is a preRequiste of some another course then it will not return False
            
            # we are making this crs PreRequisites empty [] because after visting all its preRequisites we noticed there is no cycle present. So,this course can be completed and we don't have to go through the whole process again.
            
            # Now we will append the crs in the order
            op.append(crs)
            return True
        
        for crs in range(nums):
            if not dfs(crs): return []
            
        return op
            
        
        
            
                
                
            