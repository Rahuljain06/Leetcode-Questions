class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums2 = nums * 2
        d={}
        st=[]
        res=[]
        for x in nums2:
            while st and st[-1]<x:
                a=st.pop()
                d[a]=d.get(a,[])+[x]
            st.append(x)
        for i in nums:
            if i in d and len(d[i])>0:
                res.append(d[i][0])
                d[i].pop(0)
            else:
                res.append(-1)
        return res