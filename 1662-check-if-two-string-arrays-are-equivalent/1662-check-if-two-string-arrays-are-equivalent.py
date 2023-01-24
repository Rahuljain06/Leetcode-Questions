class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i=0
        j=0
        m=0
        n=0
        
        while(i<len(word1) and j<len(word2)):
            if word1[i][m] != word2[j][n]:
                return False
            else:
                m+=1
                n+=1
            
            if m>= len(word1[i]):
                i+=1
                m=0
                
            if n>= len(word2[j]):
                j+=1
                n=0
            
        return i== len(word1) and j ==len(word2)
            
        
        
        
        
        
        
        
        
        
    