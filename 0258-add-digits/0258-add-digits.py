class Solution:
    def addDigits(self, num: int) -> int:
        sum=0
        cnt=0
        while(num>0):
            sum+=num%10
            num//=10
            cnt+=1
        return self.addDigits(sum) if cnt>=2 else sum
        
        
            
        