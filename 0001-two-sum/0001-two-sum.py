class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i,n in enumerate(nums):
            
            d=target-n
            if d in hash:
                return[hash[d],i]
            hash[n]=i#hame pehli BAAR ME NHI CHALANA HAI LOOP ISLIYE HAM NEECHE INSERT KAR RHE HAI
        return   
            
       