class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        #basically ye question 3 pointer se hoga
        #left Boundary jab tak nhi badegi jab tak minK and maxK ki range se bahar ka element nhi aayega
        #minI(minimum Idx) jo bhi idx minK(3) ka ho ya maxK(5) ka ho pehle hoga
        #maxI(maximum Idx) jo bhi idx minK(3) ka ho ya maxK(5) ka ho baad me hoga
        # eg: [5 2 3]  to isme minI=0 hoga kyunki (5) 0 idx par hai and maxI=2 hoga kyunki (3) 2 idx par hai 
        #Algorithm:
        #1: to pehle ham minI and maxI and leftboundary ko -1 le lenge
        #2: fir ham array iterate karenge and minK and maxK ko dhoondenge or jaise milenge usi hisab se
        #3: ham minI and maxI ko update kar denge
        #4: tab dono minI and maxI ki value aa jayenge fir ham un dono value se minimum nikal lenge
        #5: fir jo minimum value(smaller) aayegi usko left Boundary se subtract karenge or res mai add karenge jisse hame no of subarrays mil jayegi jo left Boundary se start hogi and jo current minI and maxI ko include karke end hogi
        #6: Edge case: agar value minK(3) and maxK(5) ki range se bhar aayi to ham left Boundary ko current idx se update kar denge kyunki uss value ko include karke koi subarray nhi ban sakti
        #7: or jab leftBoundary - smaller ki valye -(ve) aayegi to ham res mai add nhi karenge jisse 6 number vala edge case handle ho jayega
        
        
        minIdx=-1
        maxIdx=-1
        leftBoundary=-1
        res=0
        for r in range(len(nums)):
            if nums[r]==minK:
                minIdx=r
            if nums[r]==maxK:
                maxIdx=r
            if nums[r]>maxK or nums[r]<minK: #5
                leftBoundary= r
            if minIdx!=-1 and maxIdx!=-1:
                smaller=min(minIdx,maxIdx) #4
                if (smaller-leftBoundary)>0:
                    res+=smaller-leftBoundary
        return res
                    
            
            
        
