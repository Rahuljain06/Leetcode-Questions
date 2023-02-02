class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d={j:i for i, j in enumerate(order)}
        
        for i in range(len(words)-1):
            a=words[i]
            b=words[i+1]
            
            flag=False
            
            for i,j in zip(a,b):
                if d[i]<d[j]:
                    flag=True
                    break
                elif d[i]>d[j]:
                    return False
            if not flag and len(a)>len(b):
                return False
        return True
                    