class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a=""
        l=list(zip(*strs))
        for i in l:
            if len(set(i))==1:
                a+=i[0]
            else:
                break
                
        return a   
        
                
        
        