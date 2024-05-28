class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
         # Create a hashmap to store counts of nums2[j] * k
        divisor_count = defaultdict(int)
        
        # Populate the hashmap with counts of nums2[j] * k
        for num in nums2:
            divisor_count[num * k] += 1
        
        good_pairs = 0
        
        # For each number in nums1, find all its divisors and check against the hashmap
        for num in nums1:
            for j in range(1, int(num ** 0.5) + 1):
                if num % j == 0:
                    # j is a divisor
                    if j in divisor_count:
                        good_pairs += divisor_count[j]
                    # num // j is also a divisor if it's different from j
                    if j != num // j and num // j in divisor_count:
                        good_pairs += divisor_count[num // j]
        
        return good_pairs

#In this Approach: we will divide the elements of nums1 by k instead of multiplying the elements of nums2 by k and store in hashmap..Although the approach its pretty similar than above but now we dont have to check the elements of nums1 which doesn't divide by k
        n = len(nums1)
        cnt = 0
        mapi = Counter(nums2)
        for i in range(n):
            if nums1[i] % k != 0:
                continue
            val = nums1[i] // k
            for j in range(1, isqrt(val) + 1):
                if val % j == 0:
                    cnt += mapi[j]
                    if j != val // j: # num // j is also a divisor if it's different from j
                         cnt += mapi[val // j]
        return cnt
       
                    