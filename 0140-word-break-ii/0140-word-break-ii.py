class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words=set(wordDict)
        res=[]
        
        # def backtrack(pos,path):
        #     if pos==len(s):
        #         res.append(curr[1:]) # ham yaha par 1 value s esiliye add kar rhe hai jisse starting ka extra space hat jayee..
        #         return
        #     path+=" "
        #     for i in range(pos,len(s)):
        #         if s[pos:i+1] in words:
        #             backtrack(i+1, path+s[pos:i+1])
        # backtrack("",0)
        # return res
        

        def backtrack(pos,path):
            if (len(s) == pos):
                res.append(' '.join(path))
                
            for i in range(pos,len(s)):   
                tmp = s[pos:i+1]
                if (tmp in words):
                    backtrack(i+1,path+[tmp])
                    
        backtrack(0,[])
        return res 
                    
            
                    
                
            