class Solution:

    def __init__(self, nums: List[int]):
        self.d=defaultdict(list) 
        for i in range(len(nums)):
            self.d[nums[i]].append(i)

    def pick(self, target: int) -> int:
        lis=self.d[target]
        return lis[random.randint(0,len(lis)-1)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)