class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def get_counts(x):
            """
            As there are only 26 alphabets, make an array of constant size = 26 
            such that its index 0 maps to letter 'a', 1 maps to 'b' and so on...
            upto index 25 that maps to letter 'z'
            
            E.g.: If we want count of letter 'c', we will get it from count[2], 
                  as index 2 maps to letter 'c'.
                  
            But how will we do the mapping?
            
            There is a function in Python that returns a corresponding integer value for a character.
            
            ord(c) => return ordinal value of character 'c'.
            
            index of a = 0 right? => ord('a') - ord('a')
            index of b = 1        => ord('b') - ord('a')
            .
            .
            .
            index of z = 25       => ord('z') - ord('a')
            
            """
            count = [0] * 26 
            for c in x:
                count[ord(c) - ord('a')] += 1
            return count
        
        
        if not words:
            return []
        
        
        i = 0
        while i < len(words) - 1:
            # just replace sort function by get_count functions
            if get_counts(words[i]) == get_counts(words[i + 1]):
                words.remove(words[i + 1])
                continue
            i += 1
        return words