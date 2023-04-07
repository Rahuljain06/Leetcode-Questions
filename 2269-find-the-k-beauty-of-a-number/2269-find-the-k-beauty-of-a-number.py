class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count=0
        s=str(num)
        for i in range(len(s)-k+1):
            a=int(s[i:i+k])
            if a!=0 and num%a==0:
                count+=1
        return count