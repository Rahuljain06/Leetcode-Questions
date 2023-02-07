class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        res=0
        d={}
        for i,r in enumerate(fruits):
            if r in d:
                d[r]+=1
            else:
                d[r]=1
            while len(d)>2:
                d[fruits[l]]-=1
                if not d[fruits[l]]:
                    d.pop(fruits[l])
                l+=1
            res=max(res,i-l+1)
        return res
    
    
    
      # l, nums, res = 0, collections.Counter(), 0
      #   for r in range(len(tree)):
      #       nums[tree[r]] += 1
      #       while len(nums) > 2:
      #           nums[tree[l]] -= 1 
      #           if not nums[tree[l]]:
      #               nums.pop(tree[l])
      #           l += 1
      #       res = max(res, r - l + 1)
      #   return res