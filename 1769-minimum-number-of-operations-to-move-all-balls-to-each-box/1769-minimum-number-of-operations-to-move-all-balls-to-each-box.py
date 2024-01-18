class Solution:
    def minOperations(self, s: str) -> List[int]:
        res=[]
        for i in range(len(s)):
            cnt=0
            for j in range(len(s)):
                if s[j]=="1":
                    cnt+=abs(i-j)
            res.append(cnt)
        return res