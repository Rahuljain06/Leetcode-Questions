class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        maxi=0
        for i in strs:
            if i.isdigit():
                
                maxi=max(maxi,int(i))
            else:
                maxi=max(maxi,len(i))
                
        return maxi