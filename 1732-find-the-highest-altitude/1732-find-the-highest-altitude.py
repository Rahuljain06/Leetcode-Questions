class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        mx=0 if gain[0]<0 else gain[0]
        c=gain[0]
        for i in range(1,len(gain)):
            c+=gain[i]
            mx=max(mx,c)
        return mx
            