class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        a=[0]*26
        for i in range(len(s1)):
            a[ord(s1[i])-ord("a")]+=1
            a[ord(s2[i])-ord("a")]-=1
        if a==[0]*26:
            return True
        print(a)
        for i in range(len(s1),len(s2)):
            a[ord(s2[i-len(s1)])-ord("a")]+=1
            a[ord(s2[i])-ord("a")]-=1
            
            if a==[0]*26:
                return True
            
        else:
            return False
        
         
            
            
            
            
            
            
                