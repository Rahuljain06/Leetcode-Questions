class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        nums=[0]*k
        d=defaultdict(set)
        for i,j in logs:
            d[i].add(j)
        for i in d:
            nums[len(d[i])-1]+=1
        return nums
                
        
        