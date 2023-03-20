class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l=0
        r=len(height)-1
        leftmax=0
        rightmax=0
        res=0
        while l<r:
            leftmax=max(leftmax,height[l])
            rightmax=max(rightmax,height[r])
            if leftmax<rightmax:
                res+=max(0,leftmax-height[l])
                l+=1
            else:
                res+=max(0,rightmax-height[r])
                r-=1
                
        return res        
        