class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={0:1}
        cursum=0
        count=0
        for i in nums:
            cursum+=i
            if cursum-k in d:
                count+=d[cursum-k]
            d[cursum]=d.get(cursum,0)+1
        return count
       
            
            
                
            
        
        
        
        