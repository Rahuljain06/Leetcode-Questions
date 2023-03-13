class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        su=0
        while i<=j:
            s=""
            if i!=j:
                s+=str(nums[i])+str(nums[j])
            else:
                s+=str(nums[i])
            i+=1
            j-=1
            su+=int(s)
        return su
            
            