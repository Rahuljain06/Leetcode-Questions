class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words=set(wordDict)
        res=[]
        def backtrack(curr,pos):
            if pos==len(s):
                res.append(curr[1:])
                return
            curr+=" "
            for i in range(pos,len(s)):
                if s[pos:i+1] in words:
                    backtrack(curr+s[pos:i+1],i+1)
        backtrack("",0)
        return res
                    
            
                    
                
            