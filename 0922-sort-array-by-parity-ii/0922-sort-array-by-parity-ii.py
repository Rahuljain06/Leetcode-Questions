class Solution:
    def sortArrayByParityII(self, a: List[int]) -> List[int]:
        i=0
        j=1
        while i<len(a) :
            if a[i]%2==0:
                i+=2
            elif a[j]%2==1:
                j+=2
            else:
                a[i],a[j]=a[j],a[i]
                i+=2
                j+=2
        return a