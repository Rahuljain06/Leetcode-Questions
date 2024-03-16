class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d={0:-1}# ye hamne esiliye dala hai jisse [0,1] wale case handle ho jaye jab pehle 0 aayega to cnt= -1 ho jayega fir 1 aayega to count=0 aa jayega par dictionary me 0 to hai nhi lekin ans to 2 ana chaiye to isko solve karne ke liye ham pehle se hi 0 count par -1 daal denge jise ja vo check karge ki 0 hai ya nhi to usse mil jayega and res mai 2 save ho jayega==> res=max(res, idx-(d[cnt])) => res=max(res,1-(-1)) ..to ye base case tha
        cnt=0
        res=0
        for i in range(len(nums)):
            if nums[i]==0:
                cnt-=1
            else:
                cnt+=1
            if cnt in d:
                res=max(res,i-d[cnt])
            else:
                d[cnt]=i

        return res
        
            
