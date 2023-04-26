class Solution:
    def addDigits(self, num: int) -> int:
        s=str(num)
        sum=0
        for i in s:
            sum+=int(i)
        if len(str(sum))==1:
            
            return sum
        else:
            
            return self.addDigits(sum)
        
        
            
        