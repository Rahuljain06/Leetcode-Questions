class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Apporach: ham isme wordDict ki list ko set me convert kar denge jisse lookup time O(1) ho jaaye and fir simple s(given string) me loop lagakar ye check karenge ki ye words(set) me hai ya nhi agar hai to waha tak ki value current path me add kar denge and jiss index tak ki string add ki hai uske agla index bactrack function me pass kar denge path ke saath i.e: backtrack(path,i+1)
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
                    
            
                    
                
            