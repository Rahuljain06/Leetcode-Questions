import numpy
class Solution:
    def transpose(self, nums: List[List[int]]) -> List[List[int]]:
        return zip(*nums)