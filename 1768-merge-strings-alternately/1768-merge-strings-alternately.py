class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=""
        m=min(len(word1),len(word2))
        for i,j in (zip(word1,word2)):
            s+=i+j
        return s+word1[m:]+word2[m:]
            
            