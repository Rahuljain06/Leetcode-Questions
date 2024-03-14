class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
# [1,2,3,4] is our array and our target is 100
# [] -> [] // Step 0. We have 0 subarrays
# [1] -> [1] // Step 1, we grow our sliding window and see that our current window is less than target, we have 1 possible contiguous subarray
# [1,2] -> [1,2], [1], [2] // Step 2. we grow our sliding window and see that our current window is less than target, by adding the 2, we can now make 3 total contiguous subarrays. (2 more than before)
# [1,2,3] -> [1,2], [1], [2], [1,2,3] , [2,3], [3] // Step 3. we grow our sliding window and see that our current window is less than target, by adding the 3, we can now make 6 total contiguous subarrays. (3 more than before)
# [1,2,3,4] -> [1,2], [1], [2], [1,2,3] , [2,3], [3], [1,2,3,4], [2,3,4], [3,4], [4] // Step 4. we grow our sliding window and see that our current window is less than target, by adding the 4, we can now make 10 total contiguous subarrays. (4 more than before)

# To hame ye pata chala har baar ek naya element add karte hai to utni subarrays or ban jati hai,to ham (right - left) + 1 se calculate kar lenge.
        l=0
        r=0
        total=1
        cnt=0
        while r<len(nums):
            total*=nums[r]
            while total>=k and l<=r:
                total//=nums[l]
                l+=1
            cnt+=r-l+1 # iss tarike se ham saare single cases bhi cover kar lenge
            r+=1
        return cnt 
            