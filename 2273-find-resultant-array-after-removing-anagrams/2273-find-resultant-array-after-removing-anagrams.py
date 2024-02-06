class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def get_counts(x):
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