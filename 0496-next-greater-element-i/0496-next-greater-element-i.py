class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        st=[]
        res=[]
        for x in nums2:
            while st and st[-1]<x:
                d[st.pop()]=x
            st.append(x)
        for i in nums1:
            if i in d:
                res.append(d[i])
            else:
                res.append(-1)
        return res
        
        