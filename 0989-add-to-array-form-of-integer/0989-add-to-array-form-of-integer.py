class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in range(len(num)-1,-1,-1):
            su=num[i]+k
            num[i]=(su)%10
            k=su//10
        while k:
            a=k%10
            num.insert(0,a)
            k//=10
        return num