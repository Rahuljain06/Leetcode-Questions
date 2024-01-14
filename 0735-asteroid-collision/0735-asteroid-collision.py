class Solution:
    def asteroidCollision(self, nums: List[int]) -> List[int]:
        st=[]
        for a in nums:
            while st and a<0 and st[-1]>0:
                diff=abs(st[-1])-abs(a)
                if diff<0:
                    st.pop() 
                elif diff>0:
                    a=0
                elif diff==0:
                    a=0
                    st.pop()
            if a:
                st.append(a)
        return st