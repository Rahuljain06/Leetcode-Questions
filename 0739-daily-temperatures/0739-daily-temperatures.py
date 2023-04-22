class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        st=[]
        for i in range(len(temperatures)):
            while st and temperatures[i]>temperatures[st[-1]]:
                a=st.pop()
                res[a]=(i-a)
            st.append(i)
        return res   
        