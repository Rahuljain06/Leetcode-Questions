class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        m=0
        count=0
        
        for i, c in enumerate(s):
            if c in vowels:
                count+=1
            if i>=k:
                if s[i-k] in vowels:
                    count-=1
            m=max(count,m)
        
        return m
                