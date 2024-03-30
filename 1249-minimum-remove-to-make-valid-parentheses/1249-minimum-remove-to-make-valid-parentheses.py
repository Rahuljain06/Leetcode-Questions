class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        s=list(s)
        i=0
        while i<len(s):
            if s[i]=="(":
                stack.append(i)
            elif s[i]==")":
                if stack:
                    stack.pop()
                else:
                    s[i]=""
            i+=1
                
          
        if len(stack)>0:
            for i in stack:
                s[i]=""
        return  "".join(s)