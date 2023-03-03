class Solution:
    def strStr(self, s: str, n: str) -> int:
        # for i in range(len(s) - len(n)+1):
        #     if s[i:i+len(n)] == n:
        #         return i
        # return -1
    
        
        
        l=0
        for r in range(len(n)-1,len(s)):
            if s[l:r+1]==n:
                return l
            l+=1
        return -1
                



            