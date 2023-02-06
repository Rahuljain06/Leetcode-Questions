class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result=[[]]
        for num in nums:
            result+=[i+[num] for i in result]
        sum=0
        for i in range(len(result)):
            count=0
            for j in range(len(result[i])):
                
                
                
                count=count^result[i][j]
            sum+=count
        return sum