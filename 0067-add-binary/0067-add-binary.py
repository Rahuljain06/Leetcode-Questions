class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        sum= ""
        c = len(a)-1
        d = len(b)-1
        
        while c >= 0 or d >= 0 or carry:
            if c >= 0:
                carry += int(a[c])
                
            if d >= 0:
                carry += int(b[d])
                
            sum = str(carry%2) + sum
            carry //= 2
            
            c -= 1
            d -= 1
            
        return sum