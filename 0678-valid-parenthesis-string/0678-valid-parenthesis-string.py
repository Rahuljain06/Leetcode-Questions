class Solution:
    def checkValidString(self, s: str) -> bool:
        #"*()("  
        # ye test case handle ke liye hame idx store karna padega star ka alag se kyunki last me stack me [3] and star me [0] bachega or to stack ka index jyada hai to False ans aayega
        st=[]
        star=[]
        for idx,i in enumerate(s):
            if i=="(":
                st.append(idx)
            elif i=="*":
                star.append(idx)
            else:
                if st and s[st[-1]]=="(":
                    st.pop()
                elif star:
                    star.pop()
                else:
                    return False
        
        while st and star:
            if st.pop()>star.pop():
                return False
        if st: return False
        return True
                