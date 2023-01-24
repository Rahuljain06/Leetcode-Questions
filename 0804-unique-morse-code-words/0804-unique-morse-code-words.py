class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        m = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        s = dict(zip("abcdefghijklmnopqrstuvwxyz",m)) # map each letter to corresponding morse code ans store it in dictionary
        res = []
        for i in words:
            a=""
            for letter in i:
                a+="".join(s[letter])
            res.append(a)
        return len(set(res))
        