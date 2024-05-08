class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        nums_sorted = sorted(nums, reverse = True)
        awards = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i) for i in range(4, len(nums) + 1)]
        num_to_award = {num : award for num, award in zip(nums_sorted, awards)}
        results = [num_to_award[num] for num in nums]
        return results