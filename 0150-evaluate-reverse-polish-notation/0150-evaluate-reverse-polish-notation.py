class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            try:
                a=int(i)
                stack.append(a)
        

            except:
                a=stack.pop()
                b=stack.pop()
                if i=="+":
                  c=a+b
                elif i=="*":
                  c=a*b
                elif i=="/":
                  c=int(float(b/a))
                  
                else:
                  c=b-a

                stack.append(c)
        
        return stack.pop()
        