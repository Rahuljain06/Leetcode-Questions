class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
#         while val in nums:
#             nums.remove(val)
#         return(len(nums))
       
        
        
        s, e = 0, len(nums) - 1
        while s <= e:
            if nums[s] == val:
                nums[s], nums[e], e = nums[e], nums[s], e - 1
            else:
                s +=1
        return s
