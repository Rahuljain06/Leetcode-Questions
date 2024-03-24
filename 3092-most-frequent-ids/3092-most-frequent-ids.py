class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        d=defaultdict(int)
        res=[0]*len(nums)
        heap=[]
        for i,val in enumerate(nums):
            d[val]+=freq[i]    
            heapq.heappush(heap,[-d[val],val])
            while heap and -heap[0][0] != d[heap[0][1]]:
                heapq.heappop(heap)
            if heap:
                res[i]=-heap[0][0]
        return res
        
            