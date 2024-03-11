class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res=0
        idx=1
        for i in range(len(num2)-1,-1,-1):
            res+=(int(num1)*int(num2[i])*idx)
            idx*=10
        return str(res)
            
            