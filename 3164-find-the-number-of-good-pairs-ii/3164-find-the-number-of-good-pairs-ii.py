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
       
                    